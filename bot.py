import asyncio
import logging

from callbacks import call
from aiogram import Bot, Dispatcher
from handlers import bot_messages, user_commands
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from dotenv import load_dotenv
from os import getenv


load_dotenv()
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING)


async def main():
	TOKEN = getenv("BOT_TOKEN")
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
