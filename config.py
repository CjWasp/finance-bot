import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "123456789").split(",")))

COURSE_NAME = "Финансовая грамотность"
TOTAL_LESSONS = 21

DAILY_REMINDER_HOUR = 10
DAILY_REMINDER_MINUTE = 0
