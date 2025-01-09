from aiogram import Bot, Dispatcher
import asyncio, logging, os
from dotenv import load_dotenv
from app.command import router

logging.basicConfig(level=logging.DEBUG)

load_dotenv ()

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

async def main():
    dp.include_routers(router)
    await dp.start_polling(bot)

asyncio.run(main())
