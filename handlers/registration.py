from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

import database as db
from keyboards import main_menu_keyboard
from config import COURSE_NAME, ADMIN_IDS

router = Router()


class RegistrationStates(StatesGroup):
    waiting_for_name = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    user = db.get_user(message.from_user.id)
    if user:
        if not user["approved"]:
            await message.answer(
                "⏳ <b>Ваша заявка на рассмотрении.</b>\n\n"
                "Ожидайте подтверждения от куратора.",
                parse_mode="HTML"
            )
            return
        await message.answer(
            f"С возвращением, <b>{user['full_name']}</b>! 👋\n"
            f"Нажмите «📚 Уроки» чтобы продолжить.",
            reply_markup=main_menu_keyboard(),
            parse_mode="HTML"
        )
        return

    await message.answer(
        f"👋 Добро пожаловать в <b>{COURSE_NAME}</b>!\n\n"
        "Давайте познакомимся. Как вас зовут? (Имя и фамилия)",
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="HTML"
    )
    await state.set_state(RegistrationStates.waiting_for_name)


@router.message(RegistrationStates.waiting_for_name)
async def process_name(message: Message, state: FSMContext, bot: Bot):
    full_name = message.text.strip()
    if len(full_name) < 2:
        await message.answer("Пожалуйста, введите настоящее имя.")
        return

    db.register_user(
        user_id=message.from_user.id,
        username=message.from_user.username or "",
        full_name=full_name
    )
    await state.clear()

    await message.answer(
        f"✅ <b>Заявка отправлена!</b>\n\n"
        f"Спасибо, <b>{full_name}</b>!\n"
        "Ожидайте подтверждения от куратора — обычно это занимает немного времени.",
        parse_mode="HTML"
    )

    # Notify all admins
    username = message.from_user.username
    username_str = f"@{username}" if username else "нет username"
    for admin_id in ADMIN_IDS:
        try:
            from aiogram.utils.keyboard import InlineKeyboardBuilder
            builder = InlineKeyboardBuilder()
            builder.button(text="✅ Одобрить", callback_data=f"approve_user:{message.from_user.id}")
            builder.button(text="❌ Отклонить", callback_data=f"reject_user:{message.from_user.id}")
            builder.adjust(2)
            await bot.send_message(
                admin_id,
                f"📬 <b>Новая заявка на курс</b>\n\n"
                f"👤 {full_name}\n"
                f"🔗 {username_str}\n"
                f"🆔 {message.from_user.id}",
                parse_mode="HTML",
                reply_markup=builder.as_markup()
            )
        except Exception:
            pass


@router.message(F.text == "❓ Помощь")
async def help_handler(message: Message):
    await message.answer(
        "📌 <b>Как пользоваться ботом:</b>\n\n"
        "• <b>📚 Уроки</b> — список уроков курса\n"
        "• <b>✏️ Сдать ДЗ</b> — отправить домашнее задание\n"
        "• <b>📊 Прогресс</b> — ваша статистика\n\n"
        "По вопросам пишите куратору курса.",
        parse_mode="HTML"
    )
