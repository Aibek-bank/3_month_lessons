from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio, logging, os, aiosmtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

async def send_email(to_email, message_body):
    message = EmailMessage()
    message.set_content(message_body)
    message['Subject'] = 'Сообщение от бота'
    message['From'] = SMTP_USER
    message['To'] = to_email

    try:
        logging.info(f"Отправка сообщение на {to_email}")
        await aiosmtplib.send(
            message,
            hostname=SMTP_SERVER,
            port=SMTP_PORT,
            start_tls=True,
            username=SMTP_USER,
            password=SMTP_PASSWORD
        )
        logging.info("Успешно отправлена")
    except Exception as e:
        logging.info("Ошибка", e)

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет я бот который отправит сообщение на почту на которую вы укажете!")

@dp.message(lambda message: "gmail.com" in message.text)
async def email(message:types.Message):
    user_email = message.text
    await message.answer(f"Я отправил сообщение на адрес {user_email}")

    email_message = "Привет это сообщение отправлена через бота"
    await send_email(user_email, email_message)
    await message.answer("Сообщение успешно отправлена")

@dp.message(lambda message: '@' not in message.text)
async def error(message:types.Message):
    await message.answer("Пожалуйста введите правильный адрес почты.")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())