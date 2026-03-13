from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

import database as db
from keyboards import admin_keyboard, review_keyboard, main_menu_keyboard
from config import ADMIN_IDS

router = Router()


def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


class BroadcastState(StatesGroup):
    waiting_for_message = State()
    waiting_for_confirm = State()


class RejectState(StatesGroup):
    waiting_for_feedback = State()


@router.message(Command("admin"))
async def admin_panel(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer("У вас нет доступа.")
        return
    stats = db.get_stats()
    await message.answer(
        f"🔧 <b>Панель администратора</b>\n\n"
        f"👥 Пользователей: {stats['total']} (активных: {stats['active']})\n"
        f"🏁 Завершили курс: {stats['done']}\n"
        f"📋 ДЗ на проверке: {stats['hw_pending']}\n"
        f"✅ ДЗ принято: {stats['hw_approved']}",
        reply_markup=admin_keyboard(),
        parse_mode="HTML"
    )


@router.message(F.text == "📈 Статистика")
async def show_stats(message: Message):
    if not is_admin(message.from_user.id):
        return
    stats = db.get_stats()
    await message.answer(
        f"📈 <b>Статистика курса</b>\n\n"
        f"👥 Всего: <b>{stats['total']}</b>\n"
        f"✅ Активных: <b>{stats['active']}</b>\n"
        f"🏁 Завершили: <b>{stats['done']}</b>\n"
        f"📋 ДЗ ожидает: <b>{stats['hw_pending']}</b>\n"
        f"🏆 ДЗ принято: <b>{stats['hw_approved']}</b>",
        parse_mode="HTML"
    )


@router.message(F.text == "📋 Проверить ДЗ")
async def check_homework(message: Message, bot: Bot):
    if not is_admin(message.from_user.id):
        return
    pending = db.get_pending_homework()
    if not pending:
        await message.answer("✅ Нет домашних заданий на проверку!")
        return
    await message.answer(f"📋 Заданий на проверке: <b>{len(pending)}</b>", parse_mode="HTML")
    for hw in pending[:5]:
        text = (
            f"📬 <b>ДЗ #{hw['id']}</b>\n"
            f"👤 {hw['full_name']} (@{hw['username'] or '—'})\n"
            f"📖 Урок {hw['lesson_num']}\n"
            f"📅 {hw['submitted_at'][:16]}\n\n"
            f"💬 {hw['answer'][:500]}"
        )
        if hw["file_id"]:
            try:
                await bot.send_photo(message.chat.id, hw["file_id"], caption=text,
                                     parse_mode="HTML", reply_markup=review_keyboard(hw["id"]))
            except Exception:
                await bot.send_document(message.chat.id, hw["file_id"], caption=text,
                                        parse_mode="HTML", reply_markup=review_keyboard(hw["id"]))
        else:
            await message.answer(text, parse_mode="HTML", reply_markup=review_keyboard(hw["id"]))


@router.callback_query(F.data.startswith("review:approve:"))
async def approve_hw(callback: CallbackQuery, bot: Bot):
    if not is_admin(callback.from_user.id):
        return
    hw_id = int(callback.data.split(":")[2])
    hw = db.get_homework_by_id(hw_id)
    if not hw:
        await callback.answer("ДЗ не найдено.", show_alert=True)
        return
    db.review_homework(hw_id, "approved", "Отличная работа!")
    try:
        await bot.send_message(hw["user_id"],
            f"🎉 <b>Домашнее задание #{hw_id} принято!</b>\n\nПродолжайте в том же духе! 💪",
            parse_mode="HTML")
    except Exception:
        pass
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(f"✅ ДЗ #{hw_id} принято.")
    await callback.answer()


@router.callback_query(F.data.startswith("review:reject:"))
async def reject_hw(callback: CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        return
    hw_id = int(callback.data.split(":")[2])
    hw = db.get_homework_by_id(hw_id)
    await state.update_data(hw_id=hw_id, student_id=hw["user_id"])
    await callback.message.answer(f"✏️ Напишите комментарий для студента по ДЗ #{hw_id}:")
    await state.set_state(RejectState.waiting_for_feedback)
    await callback.answer()


@router.message(RejectState.waiting_for_feedback)
async def process_rejection(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    hw_id = data["hw_id"]
    student_id = data["student_id"]
    db.review_homework(hw_id, "rejected", message.text)
    try:
        await bot.send_message(student_id,
            f"📝 <b>ДЗ #{hw_id} требует доработки</b>\n\n"
            f"💬 <b>Комментарий:</b>\n{message.text}\n\n"
            "Исправьте и отправьте снова через «✏️ Сдать ДЗ».",
            parse_mode="HTML")
    except Exception:
        pass
    await state.clear()
    await message.answer(f"❌ ДЗ #{hw_id} отклонено. Студент уведомлён.")


@router.message(F.text == "📢 Рассылка")
async def broadcast_start(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        return
    await message.answer("📢 Напишите сообщение для рассылки всем студентам:")
    await state.set_state(BroadcastState.waiting_for_message)


@router.message(BroadcastState.waiting_for_message)
async def broadcast_preview(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        return
    users = db.get_all_active_users()
    count = len(users)
    await state.update_data(broadcast_text=message.text)

    builder = InlineKeyboardBuilder()
    builder.button(text=f"✅ Да, отправить {count} студентам", callback_data="broadcast:confirm")
    builder.button(text="❌ Отмена", callback_data="broadcast:cancel")
    builder.adjust(1)

    await message.answer(
        f"📢 <b>Предпросмотр сообщения:</b>\n\n"
        f"{message.text}\n\n"
        f"─────────────────\n"
        f"Получателей: <b>{count}</b>",
        parse_mode="HTML",
        reply_markup=builder.as_markup()
    )
    await state.set_state(BroadcastState.waiting_for_confirm)


@router.callback_query(F.data == "broadcast:confirm")
async def broadcast_confirm(callback: CallbackQuery, state: FSMContext, bot: Bot):
    if not is_admin(callback.from_user.id):
        return
    data = await state.get_data()
    text = data.get("broadcast_text", "")
    users = db.get_all_active_users()
    sent = 0
    failed = 0
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(f"⏳ Отправляю {len(users)} студентам...")
    for user in users:
        try:
            await bot.send_message(
                user["user_id"],
                f"📢 <b>Сообщение от куратора:</b>\n\n{text}",
                parse_mode="HTML"
            )
            sent += 1
        except Exception:
            failed += 1
    await state.clear()
    await callback.message.answer(f"✅ Готово! Отправлено: {sent}, ошибок: {failed}")
    await callback.answer()


@router.callback_query(F.data == "broadcast:cancel")
async def broadcast_cancel(callback: CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        return
    await state.clear()
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer("❌ Рассылка отменена.")
    await callback.answer()


@router.message(F.text == "🔙 Выйти из админки")
async def exit_admin(message: Message):
    if not is_admin(message.from_user.id):
        return
    await message.answer("Вышли из режима администратора.", reply_markup=main_menu_keyboard())


@router.message(Command("getfileid"))
async def get_file_id_start(message: Message):
    if not is_admin(message.from_user.id):
        return
    await message.answer(
        "📎 Отправьте мне фото — я верну его <b>file_id</b>.\n\n"
        "Можно отправлять по одному или несколько подряд.",
        parse_mode="HTML"
    )


@router.message(F.photo)
async def handle_photo(message: Message):
    if not is_admin(message.from_user.id):
        return
    file_id = message.photo[-1].file_id
    await message.answer(
        f"✅ <b>file_id:</b>\n<code>{file_id}</code>",
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("approve_user:"))
async def approve_user(callback: CallbackQuery, bot: Bot):
    if not is_admin(callback.from_user.id):
        return
    user_id = int(callback.data.split(":")[1])
    user = db.get_user(user_id)
    if not user:
        await callback.answer("Пользователь не найден.", show_alert=True)
        return
    db.approve_user(user_id)
    try:
        from keyboards import main_menu_keyboard
        await bot.send_message(
            user_id,
            "✅ <b>Ваша заявка одобрена!</b>\n\n"
            "Добро пожаловать на курс! Нажмите «📚 Уроки» чтобы начать.",
            parse_mode="HTML",
            reply_markup=main_menu_keyboard()
        )
    except Exception:
        pass
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(f"✅ {user['full_name']} одобрен.")
    await callback.answer()


@router.callback_query(F.data.startswith("reject_user:"))
async def reject_user_cb(callback: CallbackQuery, bot: Bot):
    if not is_admin(callback.from_user.id):
        return
    user_id = int(callback.data.split(":")[1])
    user = db.get_user(user_id)
    if not user:
        await callback.answer("Пользователь не найден.", show_alert=True)
        return
    name = user["full_name"]
    db.reject_user(user_id)
    try:
        await bot.send_message(
            user_id,
            "❌ <b>Ваша заявка отклонена.</b>\n\n"
            "По вопросам обращайтесь к куратору: @sergofinance",
            parse_mode="HTML"
        )
    except Exception:
        pass
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(f"❌ {name} отклонён.")
    await callback.answer()
