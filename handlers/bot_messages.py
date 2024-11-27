from aiogram import Router, F
from aiogram.types import Message
from keyboards.inline import inline_button


router = Router()


@router.message(F.text == "My keyboard.")
async def qwerty(message: Message):
	text = "Your password is: <b>qwerty</b>"
	await message.answer(text=text, reply_markup=inline_button)
