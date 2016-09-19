from peewee import (
    SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField
)

db = SqliteDatabase('../scrapy.db')


class BaseModel(Model):
    class Meta:
        database = db


class Review(BaseModel):
    pass


class Property(BaseModel):
    id = CharField(primary_key=True)
    location = IntegerField()
    ranking = IntegerField()
    name = CharField()
    url = CharField()
    reviews = ForeignKeyField(
        Review,
        related_name='prop',
        on_delete='CASCADE'
    )
