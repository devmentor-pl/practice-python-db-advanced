from db import session

from sqlalchemy.exc import SQLAlchemyError

from models import Person, Skill, clear_database


def main():
    with session:
        try:
            person1 = Person(name="Pawel")
            person2 = Person(name="Jan")
            
            skill1 = Skill(title="Programowanie")
            skill2 = Skill(title="Gotowanie")
            skill3 = Skill(title="Plywanie")
            
            session.add_all([person1, person2, skill1, skill2, skill3])
            session.commit()
            
            person1.skills.append(skill1)
            person1.skills.append(skill2)
            
            person2.skills.append(skill3)
            
            session.commit()
            
            # Dla jednej osoby wypisz listę jej umiejętności.
            result = session.query(Person).filter(Person.name == "Pawel").first()
            
            print(f"Drogi {result.name}, o to Twoje umiejętności: ")
            for skill in result.skills:
                print(f"{skill.title}")
            
            print()
            # Dla jednej umiejętności wypisz listę osób, które ją posiadają.
            result2 = session.query(Skill).filter_by(id=1).first()
            
            print(f"Umiejętność {result2.title} mają takie osoby: ")
            for person in result2.persons:
                print(f"{person.name}")
            
            
        except SQLAlchemyError as e:
            print(f"Error: {e}")
             
    clear_database()

if __name__ == "__main__":
    main()