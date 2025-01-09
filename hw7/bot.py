from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging
from config import token
from handlers import register_handlers
from scheduler import start_scheduler

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher()

# Register handlers
register_handlers(dp)

# Main function to start polling
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        # Start the scheduler in the background
        asyncio.create_task(start_scheduler(bot))
        # Run the bot
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')
