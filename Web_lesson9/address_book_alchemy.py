from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey, String, Text, Table
from sqlalchemy.orm import relationship, backref

engine = create_engine('postgresql+psycopg2://postgres:alinka@localhost:5432/address_book_db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

contacts_phones_association = Table('contact_phone', Base.metadata,
                                    Column('contact_id', Integer, ForeignKey('contact.id')),
                                    Column('phone_id', Integer, ForeignKey('phone.id'))
                                    )

contacts_emails_association = Table('contact_email', Base.metadata,
                                    Column('contact_id', Integer, ForeignKey('contact.id')),
                                    Column('email_id', Integer, ForeignKey('email.id'))
                                    )

contacts_addresses_association = Table('contact_address', Base.metadata,
                                       Column('contact_id', Integer, ForeignKey('contact.id')),
                                       Column('address_id', Integer, ForeignKey('address.id'))
                                       )


class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth_date = Column(Date)

    def __init__(self, name, surname, birth_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __repr__(self):
        return f'{self.name}_{self.surname}'


class Phone(Base):
    __tablename__ = "phone"
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    contact = relationship("Contact", secondary=contacts_phones_association)

    def __init__(self, phone):
        self.phone = phone

    def __repr__(self):
        return f'{self.phone}'


class Email(Base):
    __tablename__ = "email"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    contact = relationship("Contact", secondary=contacts_emails_association)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return f'{self.email}'


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    address = Column(Text)
    contact = relationship("Contact", secondary=contacts_addresses_association)

    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return f'{self.address}'
