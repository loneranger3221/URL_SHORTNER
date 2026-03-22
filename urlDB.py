
''' SQLite is a lightweight, serverless database engine, while SQLAlchemy is a Python library and Object-Relational Mapper (ORM) that provides a higher-level interface for interacting with databases like SQLite.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine=create_engine('sqlite:///urlshortener.db')
Base=declarative_base()#This line creates a base class for our database models using SQLAlchemy's declarative system. By inheriting from this base class, we can define our database tables as Python classes, and SQLAlchemy will handle the underlying database interactions for us.

from sqlalchemy import Column, Integer, String

class URL(Base):
    __tablename__ = "urls" #
    
    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, unique=True, index=True)
    original_url = Column(String)
    '''This class defines a database model for storing URL mappings. By defining this model, we can easily interact with the database using SQLAlchemy's ORM features.'''
    
Base.metadata.create_all(bind=engine) #This line creates the necessary database tables based on the defined models. It uses the metadata from the Base class to generate
'''bind the engine to the metadata, allowing SQLAlchemy to know which database to connect to when creating the tables.'''

from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine) #This line creates a session factory that will be used to create database sessions for interacting with the database.


'''We need a database to ensure persistence of URL mappings beyond application runtime, enable scalability, and support concurrent access instead of relying on in-memory storage.

   Why did you use SQLAlchemy? ORM
Say:(ORM)-> Object Relational Mapping.
“I used SQLAlchemy as an ORM to abstract database interactions, improve code maintainability, and enable easy scalability across different databases without rewriting SQL queries.'''