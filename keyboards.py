from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Уроки"), KeyboardButton(text="✏️ Сдать ДЗ")],
            [KeyboardButton(text="📊 Прогресс"), KeyboardButton(text="❓ Помощь")],
        ],
        resize_keyboard=True
    )


def admin_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Проверить ДЗ"), KeyboardButton(text="📢 Рассылка")],
            [KeyboardButton(text="👥 Студенты"), KeyboardButton(text="📈 Статистика")],
            [KeyboardButton(text="🔙 Выйти из админки")],
        ],
        resize_keyboard=True
    )


def review_keyboard(hw_id: int):
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Принять", callback_data=f"review:approve:{hw_id}")
    builder.button(text="❌ Отклонить с комментарием", callback_data=f"review:reject:{hw_id}")
    builder.adjust(2)
    return builder.as_markup()
