from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Measurement(Base):
    __tablename__ = "measurements"
    
    id = Column(Integer, primary_key=True)
    device_name = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp  = Column(DateTime(timezone=True), nullable=False, default=func.now())
    