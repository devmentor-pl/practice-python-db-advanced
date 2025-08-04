from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

con_str = "postgresql+psycopg2://postgres:grosales@localhost:5432/postgres"

engine = create_engine(con_str)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Note(Base):

    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    pinned = Column(Boolean, nullable=False, default=False)


Base.metadata.create_all(engine)

note_1 = Note(
    title='notatka_1',
    body='treść notatki',
    pinned=True
)

note_2 = Note(
    title='notatka_2',
    body='treść notatki 2',
    pinned=False
)


session.add_all([note_1, note_2])
session.commit()

note = session.query(Note).filter_by(title='notatka_1').first()
print(note)

note.pinned = False
session.commit()

second_note = session.query(Note).filter_by(title='notatka_2').first()
session.delete(second_note)
session.commit()

session.close()
