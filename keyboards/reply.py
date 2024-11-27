from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


my_keyboard = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="My keyboard.")
		],
	],
	resize_keyboard=True,
	one_time_keyboard=True,
	input_field_placeholder="Select an action from the menu:",
	selective=True
)
