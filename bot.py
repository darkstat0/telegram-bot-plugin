import asyncio

from callbacks import call
from aiogram import Bot, Dispatcher
from handlers import bot_messages, user_commands
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from keyboards import reply


async def main():
	TOKEN = "6447465555:AAG6qCFU4FMolxpZcIglPv1az_IJYr1zkIo"
	mode = ParseMode.HTML
	HTML = DefaultBotProperties(parse_mode=mode)
	bot = Bot(token=TOKEN, default=HTML)
	dp = Dispatcher()

	dp.include_routers(
		user_commands.router,
		call.router,
		bot_messages.router
	)

	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main=main())
