import asyncio
import logging
import random as r
from app.handlers import router
from config_read import config as c
from aiogram import Bot, Dispatcher
from aiogram.methods import SetMyCommands
from aiogram.types import BotCommand
logging.basicConfig(level=logging.INFO)
my_bot = Bot(token= c.bot_token.get_secret_value())

dp = Dispatcher()

async def main():

    bot_commands = [
        BotCommand(command="/start", description="Run bot")
        ]

    await my_bot(SetMyCommands(commands=bot_commands))

    dp.include_router(router)

    await dp.start_polling(my_bot)



if __name__ == "__main__":
    asyncio.run(main())