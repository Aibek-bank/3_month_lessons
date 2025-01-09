from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from db import add_user, add_task, set_task_time, get_schedules, delete_task, update_task

def register_handlers(dp: Dispatcher):
    dp.message.register(start_command, CommandStart())
    dp.message.register(task_command, Command('task'))
    dp.message.register(set_schedule_command, Command('set_schedule'))
    dp.message.register(view_schedule_command, Command('view_schedule'))
    dp.message.register(delete_schedule_command, Command('delete_schedule'))
    dp.message.register(update_schedule_command, Command('update_schedule'))

async def start_command(message: Message):
    add_user(message.from_user.id)
    await message.answer("Вы успешно зарегистрированы! Используйте команду /task, чтобы добавить задачу.")

async def task_command(message: Message):
    await message.answer('Введите задачу:')
    message.bot.register_message_handler(save_task, content_types=types.ContentType.TEXT)

async def save_task(message: Message):
    add_task(message.from_user.id, message.text)
    await message.answer("Задача успешно добавлена! Воспользуйтесь командами: ...")

async def set_schedule_command(message: Message):
    await message.answer('Введите время для задачи в формате ЧЧ:ММ')
    message.bot.register_message_handler(save_time, content_types=types.ContentType.TEXT)

async def save_time(message: Message):
    set_task_time(message.from_user.id, message.text)
    await message.answer("Время задачи установлено.")

async def view_schedule_command(message: Message):
    schedules = get_schedules(message.from_user.id)
    if schedules:
        await message.answer(f"Ваше расписание:\n{schedules}")
    else:
        await message.answer("Ваше расписание пусто.")

async def delete_schedule_command(message: Message):
    time = message.get_args()
    delete_task(message.from_user.id, time)
    await message.answer(f"Задача на {time} удалена.")

async def update_schedule_command(message: Message):
    args = message.get_args().split()
    if len(args) == 2:
        old_time, new_time = args
        update_task(message.from_user.id, old_time, new_time)
        await message.answer(f"Время задачи изменено с {old_time} на {new_time}.")
    else:
        await message.answer("Неверное количество аргументов.")
