from peewee import (
    SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField
)

db = SqliteDatabase('./scrapy.db')


class BaseModel(Model):
    class Meta:
        database = db


class Property(BaseModel):
    id = CharField(primary_key=True)
    location = IntegerField()
    ranking = IntegerField()
    name = CharField()
    url = CharField()

    # reviews

    @classmethod
    def from_item(cls, item):
        return cls.get_or_create(
            id=item['id'],
            location=item['location'],
            ranking=item['ranking'],
            name=item['name'],
            url=item['url']
        )


class Review(BaseModel):
    id = CharField(primary_key=True)
    rating = CharField()
    entry = CharField()
    prop = ForeignKeyField(
        Property,
        related_name='reviews',
        on_delete='CASCADE',
        null=True
    )

    @classmethod
    def from_item(cls, item):
        return cls.get_or_create(
            id=item['id'],
            rating=item['rating'],
            entry=item['entry']
        )
