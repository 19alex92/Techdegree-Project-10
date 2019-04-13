from peewee import *

DATABASE = SqliteDatabase('todo.sqlite')


class Todo(Model):
    name = CharField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect(reuse_if_open=True)
    DATABASE.create_tables([Todo], safe=True)
    DATABASE.close()
