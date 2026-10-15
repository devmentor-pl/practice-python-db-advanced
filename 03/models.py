from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

person_skill_table = Table(
    "person_skill",
    Base.metadata,
    Column("person_id", Integer, ForeignKey("persons.id", ondelete="CASCADE"), primary_key=True),
    Column("skill_id", Integer, ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True)
)

class Person(Base):
    __tablename__ = "persons"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    skills = relationship("Skill", secondary=person_skill_table, back_populates="persons")
    
class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    
    persons = relationship("Person", secondary=person_skill_table, back_populates="skills")
           