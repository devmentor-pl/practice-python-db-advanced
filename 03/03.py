from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Table

con_str = "postgresql+psycopg2://postgres:grosales@localhost:5432/postgres"

engine = create_engine(con_str)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

person_skill = Table(
    'skill_groups',
    Base.metadata,
    Column('person_id', Integer, ForeignKey('persons.id')),
    Column('skill_id', Integer, ForeignKey('skills.id'))
)


class Person(Base):

    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    skill = relationship('Skill', secondary=person_skill,
                         back_populates='person')


class Skill(Base):

    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    person = relationship(
        'Person', secondary=person_skill, back_populates='skill')


Base.metadata.create_all(engine)


skill1 = Skill(name='skill1')
skill2 = Skill(name='skill2')
skill3 = Skill(name='skill3')

person1 = Person(name='person1', skill=[skill1, skill2])
person2 = Person(name='person2', skill=[skill3, skill2])

session.add_all([skill1, skill2, skill3, person1, person2])
session.commit()

person_search = session.query(Person).filter(Person.name == 'person1').first()

if person_search:
    for skill in person_search.skill:
        print(skill.name)


skill_search = session.query(Skill).filter(Skill.name == 'skill1').first()

if skill_search:
    for person in skill_search.person:
        print(person.name)

session.close()
