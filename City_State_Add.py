from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient(
    'mongodb+srv://skom:access123@cluster0.5vezi.mongodb.net/test')
result = client['rentals_test_drop']['testing'].aggregate([
    {
        '$set': {
            'City': {
                '$arrayElemAt': [
                    {
                        '$split': [
                            '$key', ', '
                        ]
                    }, 0
                ]
            },
            'State': {
                '$arrayElemAt': [
                    {
                        '$split': [
                            '$key', ', '
                        ]
                    }, 1
                ]
            }
        }
    }
])
