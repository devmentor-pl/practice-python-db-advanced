from db import Session, engine
from models import Base, Person, Skill

Base.metadata.create_all(engine)
session = Session()

# 1. Dodaj kilka osób i kilka umiejętności.
person1 = Person(name="Kyle Reese")
person2 = Person(name="T-800")
person3 = Person(name="T-1000")
skill1 = Skill(name="Strzelanie")
skill2 = Skill(name="Samonaprawa")
skill3 = Skill(name="Ciekły metal")
skill4 = Skill(name="Podróż w czasie")
skill5 = Skill(name="Empatia")
session.add_all([person1, person2, person3, skill1, skill2, skill3, skill4, skill5])
session.commit()

# 2. Przypisz osobom wybrane umiejętności.
skill1.persons.extend([person1, person2, person3])
skill2.persons.extend([person2, person3])
skill3.persons.extend([person3])
skill4.persons.extend([person1, person2, person3])
skill5.persons.extend([person1])
session.commit()

# 3. Dla jednej osoby wypisz listę jej umiejętności.
skills_person1 = session.query(Skill).join(Skill.persons).filter(Person.name == "Kyle Reese").all()
print("Lista umiejętności Kyle Reese:")
for skill in skills_person1:
    print(skill.name)

# 4. Dla jednej umiejętności wypisz listę osób, które ją posiadają.
skills_person2 = session.query(Person).join(Person.skills).filter(Skill.name == "Samonaprawa").all()
print("\nPotrafią się samonaprawiać:")
for person in skills_person2:
    print(person.name)

session.close()