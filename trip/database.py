from peewee import (
    SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField
)

db = SqliteDatabase('./scrapy.db')


class BaseModel(Model):
    class Meta:
        database = db


class Review(BaseModel):
    id = CharField(primary_key=True)
    rating = CharField()
    entry = CharField()
    # 'prop' related name from Property

    @classmethod
    def from_item(cls, item):
        return cls.create(
            id=item['id'],
            rating=item['rating'],
            entry=item['entry']
        )


class Property(BaseModel):
    id = CharField(primary_key=True)
    location = IntegerField()
    ranking = IntegerField()
    name = CharField()
    url = CharField()
    reviews = ForeignKeyField(
        Review,
        related_name='prop',
        on_delete='CASCADE',
        null=True
    )

    @classmethod
    def from_item(cls, item):
        return cls.create(
            id=item['id'],
            location=item['location'],
            ranking=item['ranking'],
            name=item['name'],
            url=item['url']
        )
