from config import TRYS_COUNT_DEFAULT, MIN_VALUE, MAX_VALUE
from db import User


def gen_start_message_for_user(user: User, create: bool):
    assets = {
        False: "У тебя осталось всего {} из {} попыток".format(
            user.trys_count, TRYS_COUNT_DEFAULT),
        True: "У тебя есть {} попытки".format(user.trys_count)}
    if user.trys_count == 0:
        return "Извини, твои попытки кончились, повезет в другой раз"
    else:
        return ("{}. Тебе нужно отгадать "
                "Случайное число от {} до {}. Удачи ☘️").format(
            assets[create],
            MIN_VALUE, MAX_VALUE
        )
