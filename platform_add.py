from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient(
    'mongodb+srv://skom:access123@cluster0.5vezi.mongodb.net/test')
result = client['rentals_test_drop']['testing'].update_many(
    {}, {'$set': {"poop": {'$arrayElemAt': [{"$split": ["$key", ", "]}, 0]}}})
print(result.modified_count, "documents updated.")

# print all the documents
for doc in client['rentals_test_drop']['testing'].find():
    print(doc)
