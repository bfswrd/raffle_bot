import asyncio

from aiogram import Dispatcher
from aiogram.types import Message

from handlers.assets import gen_start_message_for_user
from config import RANDOM_VALUE
from db import User, check_user
from logger import logger
from misc import is_int


async def start_msg(message: Message):
    logger.info(f"{message.from_user.id}")
    user, create = User.get_or_create(user_id=message.from_user.id,
                                      name=message.from_user.username)
    await message.answer(gen_start_message_for_user(user, create))


async def notify_everyone(username: str, message: Message):
    users = User.select().dicts()
    notify = "Победил @{} 🥳🥳🥳".format(username)
    users = users.execute()
    c = 0
    for i in users:
        c += 1
        if c % 20 == 0:
            await asyncio.sleep(5)
        try:
            await message.bot.send_message(i["user_id"], notify)
        except Exception as ex:
            print(ex)


async def try_to_guess(message: Message):
    logger.info(f"{message.from_user.id}| {message.text}")
    if not is_int(message.text):
        await message.answer("Пиши число, а то забаню 👹")
        return
    if int(message.text) == RANDOM_VALUE:
        await notify_everyone(message.from_user.username, message)
        exit(0)

    user = User.get(user_id=message.from_user.id,
                    name=message.from_user.username)
    user.trys_count -= 1
    user.save()
    if user.trys_count != 0:
        await message.answer(
            "Не повезло осталось {} попытки".format(user.trys_count))
    else:
        await start_msg(message)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_msg, commands=["start"])
    dp.register_message_handler(try_to_guess, check_user)
    dp.register_message_handler(start_msg)
