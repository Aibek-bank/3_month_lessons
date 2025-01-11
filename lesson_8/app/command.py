from aiogram import Router, types
from app.parsing import get_news
from aiogram.filters import Command
import logging

router = Router()

@router.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет я бот который выводит новости!\nДля получание новости нажмите на команду /news")

@router.message(Command("news"))
async def news(message:types.Message):
    try:
        news = get_news()
        if news:
            await message.answer("\n\n".join(news))
        else:
            await message.answer("Новостей не найдено")

    except Exception as e:
        logging.error(f"Ошибка при парсинга новостей: {e}")
        await message.answer("Произошла ошибка при получение новостей")