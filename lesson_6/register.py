from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()

class Register(StatesGroup):
    last_name = State()
    first_name = State()
    gender = State()
    age = State()
    phone_number = State()
    email = State()

@router.message(F.text == "Регистрация")
async def last_name(message:types.Message, state:FSMContext):
    await message.answer("Введите вашу фамилию: ")
    await state.set_state(Register.last_name)

@router.message(Register.last_name)
async def first_name(message:types.Message, state:FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Введите ваше имя: ")
    await state.set_state(Register.first_name)

@router.message(Register.first_name)
async def gender(message:types.Message, state:FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Ваш пол (муж/жен)")
    await state.set_state(Register.gender)

@router.message(Register.gender)
async def age(message:types.Message, state:FSMContext):
    if message.text.lower() not in ["муж", "жен"]:
        await message.answer("Пожалуйста, укажите пол как 'мужской' или 'женский'.")
        return
    await state.update_data(gender=message.text.lower())
    await message.answer("Введите ваш возраст: ")
    await state.set_state(Register.age)

@router.message(Register.age)
async def phone_number(message:types.Message, state:FSMContext):
    if not message.text.isdigit():
        await message.answer("Возраст должен быть числом")
        return
    await state.update_data(age=int(message.text))
    await message.answer("Введите номер телефона")
    await state.set_state(Register.phone_number)

@router.message(Register.phone_number)
async def email(message:types.Message, state:FSMContext):
    await state.set_state(Register.phone_number)
    if not message.text.isdigit() or len(message.text) < 10:
        await message.answer("Введите корректный номер телефона:")
        return
    await state.update_data(phone_number=message.text)
    await message.answer("Введите ваш email: ")
    await state.set_state(Register.email)

@router.message(Register.email)
async def end(message:types.Message, state:FSMContext):
    if "@" not in message.text or "." not in message.text:
        await message.answer("Введите корректный email:")
        return
    await state.update_data(email=message.text)
    user_data = await state.get_data()
    summary = (
        f"Регистрация завершена\n"
        f"Фамилия: {user_data['last_name']}\n"
        f"Имя: {user_data['first_name']}\n"
        f"Пол: {user_data['gender']}\n"
        f"Возраст: {user_data['age']}\n"
        f"Телефон: {user_data['phone_number']}\n"
        f"Email: {user_data['email']}"
    )
    await message.answer(summary)
    await state.clear()