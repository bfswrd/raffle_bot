from aiogram import Bot, Dispatcher, executor

from handlers import register_handlers
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot=bot)


def main():
    register_handlers(dp)
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
