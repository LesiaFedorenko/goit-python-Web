import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    surname = Column(String(250), nullable=False)
    phone = Column(String(250))
    birthday = Column(String(250))
    email = Column(String(250))
    address = Column(String(400))


engine = create_engine('sqlite:///addressbook.db')

Base.metadata.create_all(engine)
