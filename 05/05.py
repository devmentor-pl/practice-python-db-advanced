from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, func

con_str = "postgresql+psycopg2://postgres:grosales@localhost:5432/postgres"

engine = create_engine(con_str)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Item(Base):

    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    priority = Column(Integer, default=5)


Base.metadata.create_all(engine)

items = [
    Item(name="Zadanie 1", priority=3),
    Item(name="Zadanie 2", priority=1),
    Item(name="Zadanie 3", priority=5),
    Item(name="Zadanie 4", priority=2),
    Item(name="Zadanie 5", priority=4),
    Item(name="Zadanie 6", priority=3),
    Item(name="Zadanie 7", priority=2),
    Item(name="Zadanie 8", priority=1),
    Item(name="Zadanie 9", priority=4),
    Item(name="Zadanie 10", priority=5),
    Item(name="Zadanie 11", priority=2),
    Item(name="Zadanie 12", priority=3),
    Item(name="Zadanie 13", priority=1),
    Item(name="Zadanie 14", priority=4),
    Item(name="Zadanie 15", priority=5),
    Item(name="Zadanie 16", priority=2),
    Item(name="Zadanie 17", priority=1),
    Item(name="Zadanie 18", priority=3),
    Item(name="Zadanie 19", priority=4),
    Item(name="Zadanie 20", priority=2),
]

session.add_all(items)
session.commit()

sorted_tasks = session.query(Item).order_by(Item.priority).all()

print(sorted_tasks)

mid_priority_elements = session.query(Item).limit(5).offset(10).all()

session.close()
