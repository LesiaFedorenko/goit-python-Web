from pymongo import MongoClient, DESCENDING, ASCENDING

client = MongoClient(
    'mongodb+srv://fedorenkolesia:AuP6sZpCSyr0FIMA@cluster0.abuuj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

with client:
    db = client.addressbookdb

    contacts = db.contacts.find()
    for contact in contacts:
        print(f'{contact["name"]} phone: {contact["phone"]}')

    query_1 = db.contacts.find().sort("birth_date", DESCENDING).limit(3)
    [print(contact['name'], contact['birth_date']) for contact in query_1]

    query_2 = db.contacts.find().sort("birth_date", ASCENDING).limit(3)
    [print(contact['name'], contact['birth_date']) for contact in query_2]

    query_3 = db.contacts.find({'birth_date': {'$gte': '2005-01-01', '$lt': '2013-01-01'}})

    [print(contact['name'], contact['birth_date']) for contact in query_3]
