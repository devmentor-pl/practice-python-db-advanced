from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime

from db import engine


Base = declarative_base()

class Measurement(Base):
    __tablename__ = "measurements"
    
    id = Column(Integer, primary_key=True)
    device_name = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    
 
Base.metadata.create_all(engine)

def clear_database():
    Base.metadata.drop_all(engine)