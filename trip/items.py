from scrapy import Item, Field


class ReviewItem(Item):
    pass


class PropertyItem(Item):
    id = Field()
    location = Field()
    ranking = Field()
    name = Field()
    url = Field()
