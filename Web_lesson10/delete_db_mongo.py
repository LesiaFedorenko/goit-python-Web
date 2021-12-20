from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://fedorenkolesia:AuP6sZpCSyr0FIMA@cluster0.abuuj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

with client:
    db = client.addressbookdb

    contacts = db.contacts

    d = contacts.delete_one({'name': 'Ana'})

    print(d,  ' contact deleted')
