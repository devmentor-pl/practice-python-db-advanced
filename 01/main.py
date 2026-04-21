from db import Session, engine

from models import Base, Note


Base.metadata.create_all(engine)


session = Session()

new_note = Note(title="Test Note", body="Some body of testing note")
new_note2 = Note(title="second note", body="Body of second note")

session.add_all([new_note, new_note2])

session.commit()

first_note = session.query(Note).filter(Note.title == "Test Note").first()

print(first_note.title)

update_note = session.query(Note).filter_by(id=1).first()
update_note.pinned = True
session.commit()

delete_note = session.query(Note).filter_by(id=2).first()
session.delete(delete_note)
session.commit()

session.close()
