from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table

from db import engine


Base = declarative_base()


person_skill = Table(
    "person_skill", 
    Base.metadata,
    Column("person_id", Integer, ForeignKey("persons.id")),
    Column("skill_id", Integer, ForeignKey("skills.id")),
    )



class Person(Base):
    __tablename__ = "persons"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    skills = relationship("Skill", secondary=person_skill, back_populates="persons")
     
    
class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    
    persons = relationship("Person", secondary=person_skill, back_populates="skills")
    

Base.metadata.create_all(engine)

def clear_database():
    Base.metadata.drop_all(engine)