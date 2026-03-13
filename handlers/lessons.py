from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

import database as db
from course_content import LESSONS, MODULES, MODULE_BREAK_MESSAGE, FINAL_MESSAGE, FINAL_COVER, TOTAL_LESSONS
from keyboards import main_menu_keyboard

router = Router()


def get_lesson(lesson_id: int) -> dict | None:
    return next((l for l in LESSONS if l["id"] == lesson_id), None)


def get_module_lessons(module_num: int) -> list:
    return [l for l in LESSONS if l["module"] == module_num]


def get_current_module(lesson_id: int) -> int:
    lesson = get_lesson(lesson_id)
    return lesson["module"] if lesson else 1


def lesson_keyboard_before_watch(lesson: dict):
    """Keyboard before student clicks watch — no finish button yet."""
    builder = InlineKeyboardBuilder()
    builder.button(
        text="▶️ Смотреть урок",
        callback_data=f"watch_lesson:{lesson['id']}"
    )
    if lesson["extra_video_url"]:
        builder.button(
            text=f"🔗 {lesson['extra_video_label']}",
            url=lesson["extra_video_url"]
        )
    if lesson["hw_type"] == "text":
        builder.button(
            text="✏️ Выполнить задание",
            callback_data=f"hw_start:{lesson['id']}"
        )
    builder.adjust(1)
    return builder.as_markup()


def lesson_keyboard_after_watch(lesson: dict):
    """Keyboard after student clicked watch — finish button appears."""
    builder = InlineKeyboardBuilder()
    builder.button(
        text="▶️ Смотреть урок",
        callback_data=f"watch_lesson:{lesson['id']}"
    )
    if lesson["extra_video_url"]:
        builder.button(
            text=f"🔗 {lesson['extra_video_label']}",
            url=lesson["extra_video_url"]
        )
    if lesson["hw_type"] == "text":
        builder.button(
            text="✏️ Выполнить задание",
            callback_data=f"hw_start:{lesson['id']}"
        )
    builder.button(
        text="✅ Завершить урок",
        callback_data=f"mark_done:{lesson['id']}"
    )
    builder.adjust(1)
    return builder.as_markup()


def lessons_list_keyboard(current_lesson_id: int):
    builder = InlineKeyboardBuilder()
    current_module_num = get_current_module(current_lesson_id)
    module_lessons = get_module_lessons(current_module_num)

    for lesson in module_lessons:
        lid = lesson["id"]
        if lid < current_lesson_id:
            label = f"✅ {lesson['title']}"
        elif lid == current_lesson_id:
            label = f"▶️ {lesson['title']}"
        else:
            label = f"🔒 {lesson['title']}"

        cb = f"open_lesson:{lid}" if lid <= current_lesson_id else "locked"
        builder.button(text=label, callback_data=cb)

    builder.adjust(1)
    return builder.as_markup()


async def send_lesson_message(target, lesson: dict, bot: Bot = None):
    hw_block = ""
    if lesson["hw_type"] == "text" and lesson["hw_text"]:
        hw_block = f"\n\n{lesson['hw_text']}"
    elif lesson["hw_type"] == "info" and lesson["hw_text"]:
        hw_block = f"\n\n{lesson['hw_text']}"

    caption = f"{lesson['text']}{hw_block}"
    keyboard = lesson_keyboard_before_watch(lesson)

    if lesson.get("cover"):
        await target.answer_photo(
            photo=lesson["cover"],
            caption=caption,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    else:
        await target.answer(
            caption,
            reply_markup=keyboard,
            parse_mode="HTML",
            disable_web_page_preview=True
        )


# ── Handlers ───────────────────────────────────────────────────────────────

@router.message(F.text == "📚 Уроки")
async def show_lessons_list(message: Message):
    user = db.get_user(message.from_user.id)
    if not user:
        await message.answer("Сначала зарегистрируйтесь. Нажмите /start")
        return
    if not user["approved"]:
        await message.answer("⏳ Ваша заявка ещё на рассмотрении.")
        return

    cur = user["current_lesson"]
    current_module = get_current_module(cur)
    module_lessons = get_module_lessons(current_module)
    done_in_module = len([l for l in module_lessons if l["id"] < cur])
    total_in_module = len(module_lessons)

    await message.answer(
        f"📚 <b>{MODULES[current_module]['title']}</b>\n\n"
        f"Пройдено: <b>{done_in_module}</b> из {total_in_module} уроков",
        reply_markup=lessons_list_keyboard(cur),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "noop")
async def noop(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(F.data == "locked")
async def locked_lesson(callback: CallbackQuery):
    await callback.answer("🔒 Сначала завершите текущий урок!", show_alert=True)


@router.callback_query(F.data.startswith("open_lesson:"))
async def open_lesson(callback: CallbackQuery, bot: Bot):
    lesson_id = int(callback.data.split(":")[1])
    user = db.get_user(callback.from_user.id)

    if not user or lesson_id > user["current_lesson"]:
        await callback.answer("🔒 Урок ещё не открыт!", show_alert=True)
        return

    lesson = get_lesson(lesson_id)
    if not lesson:
        await callback.answer("Урок не найден.", show_alert=True)
        return

    await send_lesson_message(callback.message, lesson, bot)
    await callback.answer()


@router.callback_query(F.data.startswith("watch_lesson:"))
async def watch_lesson(callback: CallbackQuery, bot: Bot):
    lesson_id = int(callback.data.split(":")[1])
    lesson = get_lesson(lesson_id)
    if not lesson:
        await callback.answer()
        return

    # Open the video URL in Telegram
    await bot.answer_callback_query(
        callback.id,
        url=lesson["video_url"]
    )

    # Update keyboard to show finish button
    try:
        await callback.message.edit_reply_markup(
            reply_markup=lesson_keyboard_after_watch(lesson)
        )
    except Exception:
        pass


@router.callback_query(F.data.startswith("mark_done:"))
async def mark_lesson_done(callback: CallbackQuery, bot: Bot):
    lesson_id = int(callback.data.split(":")[1])
    user = db.get_user(callback.from_user.id)

    if not user:
        await callback.answer("Ошибка. Напишите /start", show_alert=True)
        return

    lesson = get_lesson(lesson_id)
    if not lesson:
        await callback.answer("Урок не найден.", show_alert=True)
        return

    await callback.message.edit_reply_markup(reply_markup=None)

    if lesson["apps_text"]:
        await callback.message.answer(
            lesson["apps_text"],
            parse_mode="HTML",
            disable_web_page_preview=True
        )

    if lesson_id == user["current_lesson"]:
        if lesson_id >= TOTAL_LESSONS:
            db.complete_course(callback.from_user.id)
            await bot.send_photo(
                callback.from_user.id,
                photo=FINAL_COVER,
                caption=FINAL_MESSAGE,
                parse_mode="HTML"
            )
            await callback.answer()
            return

        next_lesson = get_lesson(lesson_id + 1)
        is_module_end = next_lesson and next_lesson["module"] != lesson["module"]

        db.advance_lesson(callback.from_user.id)

        if is_module_end:
            break_msg = MODULE_BREAK_MESSAGE.get(lesson["module"], "")
            if break_msg:
                await callback.message.answer(break_msg, parse_mode="HTML", reply_markup=main_menu_keyboard())
                await callback.answer()
                return

        await send_lesson_message(callback.message, next_lesson, bot)

    await callback.answer()


@router.message(F.text == "📊 Прогресс")
async def show_progress(message: Message):
    user = db.get_user(message.from_user.id)
    if not user:
        await message.answer("Сначала зарегистрируйтесь. Нажмите /start")
        return
    if not user["approved"]:
        await message.answer("⏳ Ваша заявка ещё на рассмотрении.")
        return

    cur = user["current_lesson"]
    done = cur - 1
    pct = round(done / TOTAL_LESSONS * 100)
    bar_filled = int(pct / 10)
    bar = "🟩" * bar_filled + "⬜" * (10 - bar_filled)

    lesson = get_lesson(cur)
    module_name = MODULES[lesson["module"]]["title"] if lesson else "Курс завершён"

    await message.answer(
        f"📊 <b>Ваш прогресс</b>\n\n"
        f"👤 {user['full_name']}\n"
        f"📦 {module_name}\n"
        f"✅ Пройдено: <b>{done}</b> из {TOTAL_LESSONS} уроков\n\n"
        f"{bar} {pct}%\n\n"
        f"📅 На курсе с: {user['registered_at'][:10]}",
        parse_mode="HTML",
        reply_markup=main_menu_keyboard()
    )
