from models import Base, Note
from db import engine, Session
from sqlalchemy.exc import SQLAlchemyError

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session() as session:
    try:

        new_note_1 = Note(
            title="Przepis",
            body="Mąkę wsypać do miski, dodać mleko oraz wodę..."
        )
        
        new_note_2 = Note(
            title="Zakupy",
            body="1.Jabłka, 2.Mleko, 3.Jajka",
        )
        
        session.add(new_note_1)
        session.add(new_note_2)
        
        session.commit()

        found_note_1 = session.query(Note).filter_by(title="Przepis").first()
        if found_note_1:
            print(f"Treść: {found_note_1.body}", f"Przypięta: {found_note_1.pinned}")
            found_note_1.pinned = True
        else:
            print("Nie istnieje!")
            
        found_note_2 = session.query(Note).filter_by(title="Zakupy").first()
        if found_note_2:
            print(f"Treść: {found_note_2.body}", f"Przypięta: {found_note_2.pinned}")
            session.delete(found_note_2) 
        else:
            print("Nie istnieje!")
            
        session.commit()
        
        found_note_3 = session.query(Note).filter_by(title="Przepis").first()
        if found_note_3:
            print(f"Treść: {found_note_3.body}", f"Przypięta: {found_note_3.pinned}")
        else:
            print("Nie istnieje!")
            
        found_note_4 = session.query(Note).filter_by(title="Zakupy").first()
        if found_note_4:
            print(f"Treść: {found_note_4.body}", f"Przypięta: {found_note_4.pinned}")
        else:
            print("Nie istnieje!")
        
    except SQLAlchemyError as e:
        
        session.rollback()
        print(f"Błąd: {e}")
