from db import Session, engine
from models import Note, Base

Base.metadata.create_all(engine)
session = Session()

# 1. Utwórz i zapisz do bazy dwie notatki.
note1 = Note(title="Znaleziono skarb", body="Pod Wrocławiem znaleziono skarba z czasów II Wojny Światowej", pinned=False)
note2 = Note(title="Bursztynowa Komnata odkryta", body="Po kilkudziesięciu latach od zniknięcia wreszcie odkryto miejsce ukrycia Bursztynowej Komnaty", pinned=False)

session.add(note1)
session.add(note2)
session.commit()

# 2. Wyszukaj notatkę po tytule i wypisz jej treść.
note_query = session.query(Note).filter(Note.title == "Znaleziono skarb").first()
print(note_query.title, note_query.body)

# 3. Zmień status `pinned` jednej z notatek na `True` i zapisz zmiany.
note_query.pinned = True
session.commit()

# 4. Usuń drugą notatkę z bazy.
user_delete = session.query(Note).filter(Note.title == "Bursztynowa Komnata odkryta").first()
session.delete(user_delete)
session.commit()

session.close()