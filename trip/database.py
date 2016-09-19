from peewee import (
    SqliteDatabase, Model, CharField, DateField, BooleanField
)

db = SqliteDatabase('../scrapy.db')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db