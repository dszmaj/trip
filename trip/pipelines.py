from .database import Property, Review, db
from .items import PropertyItem, ReviewItem


db.connect()
try:
    db.create_tables([Review, Property])
except:
    # no need for anything better as it basically fails only if db exists
    pass


class ReviewPipe:
    @staticmethod
    def process_item(item, spider):
        if isinstance(item, ReviewItem):
            review = Review.from_item(item)
            review.save()


class PropertyPipe:
    @staticmethod
    def process_item(item, spider):
        if isinstance(item, PropertyItem):
            prop = Property.from_item(item)
            prop.save()
