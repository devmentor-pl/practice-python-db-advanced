from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

from db import engine


Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    
 
Base.metadata.create_all(engine)

def clear_database():
    Base.metadata.drop_all(engine)