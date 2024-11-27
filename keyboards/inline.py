from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_button = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="My username",
								 callback_data="my_username")
		]
	]
)
