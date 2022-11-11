from peewee import (
    SqliteDatabase, Model,
    IntegerField, CharField, SmallIntegerField
)

from config import TRYS_COUNT_DEFAULT

conn = SqliteDatabase("data.sqlite3")


class BaseModel(Model):
    class Meta:
        database = conn


class User(BaseModel):
    user_id = IntegerField()
    name = CharField()
    trys_count = SmallIntegerField(default=TRYS_COUNT_DEFAULT)

    class Meta:
        table_name = 'users'


def check_user(message) -> bool:
    user_id = message.from_user.id
    try:
        user = User.get(User.user_id == user_id)
    except Exception:
        return False
    return user.trys_count > 0


def create_table():
    with conn:
        conn.create_tables([User])


create_table()
