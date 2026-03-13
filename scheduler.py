from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from aiogram import Bot

import database as db
from config import DAILY_REMINDER_HOUR, DAILY_REMINDER_MINUTE, TOTAL_LESSONS


async def send_daily_reminders(bot: Bot):
    users = db.get_all_active_users()
    sent = 0
    for user in users:
        if user["current_lesson"] > TOTAL_LESSONS or user.get("course_done"):
            continue
        try:
            await bot.send_message(
                user["user_id"],
                f"👋 Привет, <b>{user['full_name']}</b>!\n\n"
                f"Напоминаем — вас ждёт продолжение курса. "
                "Нажмите «📚 Мои уроки» чтобы продолжить. 🚀",
                parse_mode="HTML"
            )
            sent += 1
        except Exception:
            pass
    print(f"[Scheduler] Напоминания отправлены: {sent}")


def setup_scheduler(bot: Bot) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler(timezone="Asia/Almaty")
    scheduler.add_job(
        send_daily_reminders,
        trigger=CronTrigger(hour=DAILY_REMINDER_HOUR, minute=DAILY_REMINDER_MINUTE),
        kwargs={"bot": bot},
        id="daily_reminder",
        replace_existing=True
    )
    return scheduler
