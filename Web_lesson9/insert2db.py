from datetime import date
from faker import Faker
from address_book_alchemy import Session, engine, Base

from address_book_alchemy import Contact, Phone, Email, Address

fake = Faker()
session = Session()

contact_1 = Contact(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(1977, 12, 12)))
contact_2 = Contact(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(1977, 12, 12)))
contact_3 = Contact(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(1977, 12, 12)))
contact_4 = Contact(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(1977, 12, 12)))
contact_5 = Contact(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(1977, 12, 12)))
contact_6 = Contact(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(1977, 12, 12)))
contact_7 = Contact(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(1977, 12, 12)))

phone_1 = Phone(fake.phone_number())
phone_2 = Phone(fake.phone_number())
phone_3 = Phone(fake.phone_number())
phone_4 = Phone(fake.phone_number())
phone_5 = Phone(fake.phone_number())
phone_6 = Phone(fake.phone_number())
phone_7 = Phone(fake.phone_number())
phone_8 = Phone(fake.phone_number())
phone_9 = Phone(fake.phone_number())
phone_10 = Phone(fake.phone_number())

email_1 = Email(fake.ascii_free_email())
email_2 = Email(fake.ascii_free_email())
email_3 = Email(fake.ascii_free_email())
email_4 = Email(fake.ascii_free_email())
email_5 = Email(fake.ascii_free_email())

address_1 = Address(fake.city() + ' ' + fake.street_address() + ' ' + fake.postcode())
address_2 = Address(fake.city() + ' ' + fake.street_address() + ' ' + fake.postcode())
address_3 = Address(fake.city() + ' ' + fake.street_address() + ' ' + fake.postcode())
address_4 = Address(fake.city() + ' ' + fake.street_address() + ' ' + fake.postcode())

phone_1.contact = [contact_1]
phone_2.contact = [contact_2]
phone_3.contact = [contact_3]
phone_4.contact = [contact_4]
phone_5.contact = [contact_5]
phone_6.contact = [contact_6]
phone_7.contact = [contact_7]
phone_8.contact = [contact_1]
phone_9.contact = [contact_2]
phone_10.contact = [contact_3]


email_1.contact = [contact_1]
email_2.contact = [contact_2]
email_3.contact = [contact_3]
email_4.contact = [contact_4]
email_5.contact = [contact_5]

address_1.contact = [contact_1]
address_2.contact = [contact_2]
address_3.contact = [contact_3]
address_4.contact = [contact_4]

session.add(contact_1)
session.add(contact_2)
session.add(contact_3)
session.add(contact_4)
session.add(contact_5)
session.add(contact_6)
session.add(contact_7)

session.add(phone_1)
session.add(phone_2)
session.add(phone_3)
session.add(phone_4)
session.add(phone_5)
session.add(phone_6)
session.add(phone_7)
session.add(phone_8)
session.add(phone_9)
session.add(phone_10)

session.add(email_1)
session.add(email_2)
session.add(email_3)
session.add(email_4)
session.add(email_5)

session.add(address_1)
session.add(address_2)
session.add(address_3)
session.add(address_4)

session.commit()
session.close()
