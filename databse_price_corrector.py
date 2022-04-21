# { $substr: [ "$quarter", 0, 2 ] }
from pprint import pprint
from pydoc import doc
from pymongo import MongoClient


# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient(
    'mongodb+srv://skom:access123@cluster0.5vezi.mongodb.net/test')

database = client['rentals_test_drop']['testing']

# get all the documents in the collection with platform = 'AirBnb' and change the rental_price to the 5th character of the quarter
# rental_price = rental_price[
