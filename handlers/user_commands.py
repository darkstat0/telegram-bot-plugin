from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.reply import my_keyboard


router = Router()


@router.message(CommandStart())
async def start(message: Message):
	text = "Hello, <b>{}</b>".format(message.from_user.first_name)
	await message.answer(text=text, reply_markup=my_keyboard)


@router.message(Command("help"))
async def help(message: Message):
	text = "<b>It's the SMS for the settings!</b>"
	await message.answer(text=text)
