from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

person_skill = Table(
    "person_skill",
    Base.metadata,
    Column("person_id", Integer, ForeignKey("persons.id")),
    Column("skill_id", Integer, ForeignKey("skills.id"))
)

class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    skills = relationship("Skill", secondary=person_skill, back_populates="persons")

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    persons = relationship("Person", secondary=person_skill, back_populates="skills")

