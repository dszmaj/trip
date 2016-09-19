from peewee import (
    SqliteDatabase, Model, CharField, IntegerField
)

db = SqliteDatabase('../scrapy.db')


class Property(Model):
    id = CharField(primary_key=True)
    location = IntegerField()
    ranking = IntegerField()
    name = CharField()
    url = CharField()

    class Meta:
        database = db
