from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from db import engine


Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    books = relationship("Book", back_populates="author")
    
    
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    
    author = relationship("Author", back_populates="books")
        

Base.metadata.create_all(engine)

def clear_database():
    Base.metadata.drop_all(engine)