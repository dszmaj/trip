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
            review, created = Review.from_item(item)
            review.prop = Property.get(id=item['prop'])
            review.save()
        else:
            return item


class PropertyPipe:
    @staticmethod
    def process_item(item, spider):
        if isinstance(item, PropertyItem):
            prop, created = Property.from_item(item)
            prop.save()
        else:
            return item
