from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///database.db')

class Library(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    book_title = Column(String(100), nullable=False)
    author = Column(String(100))

Base.metadata.create_all(engine)
