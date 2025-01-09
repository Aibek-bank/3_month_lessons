from aiogram.filters import Command
from aiogram import Router, types

router = Router()



@router.message(Command("about"))
async def about(message:types.Message):
    await message.answer("Команда о нас")

@router.message(Command("info"))
async def about(message:types.Message):
    await message.answer("Информация о гиксе")

@router.message(Command("team"))
async def about(message:types.Message):
    await message.answer("Наша команда")