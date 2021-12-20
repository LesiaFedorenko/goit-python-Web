from address_book_alchemy import Session, engine, Base
from address_book_alchemy import Contact, Phone, Email, Address
from datetime import date

session = Session()

i = session.query(Contact).get(3)
i.surname = 'Fedorenko'
session.add(i)
session.commit()

