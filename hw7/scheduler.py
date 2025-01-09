import aioschedule
import asyncio
from datetime import datetime
from db import cursor

async def send_reminder(bot):
    schedules = cursor.execute("SELECT user_id, time FROM schedules").fetchall()
    for user_id, time in schedules:
        if datetime.now().strftime("%H:%M") == time:
            await bot.send_message(user_id, "Пора выполнить задачу!")

async def start_scheduler(bot):
    aioschedule.every().minute.do(send_reminder, bot)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
