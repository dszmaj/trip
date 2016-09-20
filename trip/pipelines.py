from .database import Property, Review, db


db.connect()
try:
    db.create_tables([Review, Property])
except:
    # no need for anything better as it basically fails only if db exists
    pass


class ReviewPipe:
    @staticmethod
    def process_item(item, spider):
        review = Review.from_item(item)
        review.save()


class PropertyPipe:
    @staticmethod
    def process_item(item, spider):
        prop = Property.from_item(item)
        prop.save()
