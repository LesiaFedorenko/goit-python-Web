from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://fedorenkolesia:AuP6sZpCSyr0FIMA@cluster0.abuuj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

with client:
    db = client.addressbookdb

    contacts = db.contacts

    filter_value = {'name': 'Angela'}
    new_value = {"$set": {'birth_date': '1999-03-24'}}

    contacts.update_one(filter_value, new_value)


