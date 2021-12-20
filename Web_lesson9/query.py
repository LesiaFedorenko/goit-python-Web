from address_book_alchemy import Session, engine, Base
from address_book_alchemy import Contact, Phone, Email, Address
from datetime import date

session = Session()

contacts = session.query(Contact).all()

print('All Contact:', '\n')

for contact in contacts:
    print(contact.name, contact.surname)

contact_phone = session.query(Phone).all()

for phone in contact_phone:
    print(phone)

query_1=session.query(Contact).filter(Contact.name == 'Jennifer').all()
for i in query_1:
    print(i.name, i.birth_date)

query_2=session.query(Contact).filter(Contact.birth_date > date(1976, 3, 24)).all()
for i in query_2:
    print(i.name, i.birth_date)

session.close()