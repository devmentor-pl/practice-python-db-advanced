from datetime import datetime, timedelta, timezone
from db import session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from models import Item, clear_database

ITEMS = [
    ("Mleko", 1),
    ("Chleb", 1),
    ("Jajka", 2),
    ("Masło", 2),
    ("Ser żółty", 3),
    ("Jogurt", 3),
    ("Makaron", 4),
    ("Ryż", 4),
    ("Pomidory", 5),
    ("Ogórki", 5),
    ("Cebula", 6),
    ("Czosnek", 6),
    ("Kurczak", 7),
    ("Łosoś", 7),
    ("Oliwa z oliwek", 8),
    ("Mąka", 8),
    ("Cukier", 9),
    ("Sól", 9),
    ("Kawa", 10),
    ("Herbata", 10),
]

def main():
    
    with session:
        try:
            items = [Item(name=name, priority=priority) for name, priority in ITEMS]
            session.add_all(items)
            session.commit()
            
        except SQLAlchemyError as e:
            print(f"Error: {e}")
    
    with session:
        try:
            # Posortuj elementy rosnąco po priorytecie.
            items = session.query(Item).order_by(Item.priority).all()
            for item in items:
                print(item.name, item.priority)
            
        except SQLAlchemyError as e:
            print(f"Error: {e}")    

    print()
    
    with session:
        try:
            # Zaimplementuj paginację: wypisz tylko elementy od 11 do 15 miejsca (strona 3 przy 5 elementach na stronę).
            items = session.query(Item).order_by(Item.priority).limit(5).offset(11).all()
            for item in items:
                print(item.name, item.priority)
            
        except SQLAlchemyError as e:
            print(f"Error: {e}")   
    
    clear_database()

if __name__ == "__main__":
    main()