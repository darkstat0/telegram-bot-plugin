from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.reply import my_keyboard


router = Router()


@router.callback_query(F.data == "my_username")
async def for_inline(call: CallbackQuery):
	text = f"{call.from_user.username}"
	await call.message.answer(text=text, reply_markup=my_keyboard)
