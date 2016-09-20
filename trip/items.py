from scrapy import Item, Field


class ReviewItem(Item):
    id = Field()
    rating = Field()
    entry = Field()


class PropertyItem(Item):
    id = Field()
    location = Field()
    ranking = Field()
    name = Field()
    url = Field()
