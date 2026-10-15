from models import Base, Person, Skill
from db import engine, Session
from sqlalchemy.exc import SQLAlchemyError

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session() as session:
    try:

        person_1 = Person(name="Adam")
        person_2 = Person(name="Bartek")
        person_3 = Person(name="Konrad")
        person_4 = Person(name="Patryk")
        person_5 = Person(name="Krzysztof")
        
        skill_1 = Skill(name="PostgreSQL")
        skill_2 = Skill(name="Python")
        skill_3 = Skill(name="TypeScript")
        skill_4 = Skill(name="Docker")
        skill_5 = Skill(name="PLC")
        
        person_1.skills= [skill_1, skill_2]
        person_2.skills= [skill_2, skill_3]
        person_3.skills= [skill_3, skill_4]
        person_4.skills= [skill_4, skill_5]
        person_5.skills= [skill_5]
        
        session.add_all([person_1, person_2, person_3, person_4, person_5])
        session.add_all([skill_1, skill_2, skill_3, skill_4, skill_5])

        session.commit()
        
        target_person = session.query(Person).filter(Person.name == "Adam").first()
        
        if target_person:
            for skill in target_person.skills:
                print(skill.name)
            
        target_skill = session.query(Skill).filter(Skill.name == "TypeScript").first()
        
        if target_skill:
            for person in target_skill.persons:
                print(person.name)
      
    except SQLAlchemyError as e:
        
        session.rollback()
        print(f"Błąd: {e}")
