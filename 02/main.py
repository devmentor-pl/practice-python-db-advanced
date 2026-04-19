from db import engine
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from models import Author, Book, clear_database


def create_author(name):
    return Author(name=name)

def create_book(title, author_id):
    return Book(title=title, author_id=author_id)



def main():
    with Session(engine) as session:
        try:
            pawel = create_author("Paweł T")
            jan = create_author("Jan Nowak")
            session.add_all([pawel, jan])
            session.commit()
        
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")
        
    
    with Session(engine) as session:
        try:
            author = session.query(Author).filter_by(name="Paweł T").first()
        
            book1 = create_book("Django 5", author.id)
            book2 = create_book("Django 6", author.id)
            book3 = create_book("Python od podstaw", author.id)
            
            session.add_all([book1, book2, book3])
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")
    
    
    with Session(engine) as session:
        try:
            author = session.query(Author).filter_by(name="Jan Nowak").first()
        
            book1 = create_book("Bardzo dobra ksiązka", author.id)
            book2 = create_book("Najlepsza ksiązka", author.id)
            book3 = create_book("AI nie wyprze programostów", author.id)
            book4 = create_book("AI to tylko narzędzie dla programistów", author.id)
            
            session.add_all([book1, book2, book3, book4])
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")
    
    # Pobierz i wypisz wszystkie książki konkretnego autora (np. „Jan Nowak”).
    with Session(engine) as session:
        try:
            nowak = session.query(Author).filter(Author.name == "Jan Nowak").first()
            
            if nowak:
                print("Ksiązki pana Nowaka:")
                for book in nowak.books:
                    print(book.title)
        except SQLAlchemyError as e:
            print(f"Error: {e}")
    
    print()
    
    # Pobierz listę autorów, którzy mają więcej niż jedną książkę.      
    with Session(engine) as session:
        try:
            # results = session.query(Book.author, func.count(Book.id)).group_by(Book.author_id).having(func.count(Book.id) > 1).all()
            
            results = session.query(Author.name, func.count(Book.id)).join(Book).group_by(Author.id).having(func.count(Book.id) > 1).all()
            
            for name, count in results:
                print(f"{name} -> {count} ksiązek.")
            
        except SQLAlchemyError as e:
            print(f"Error: {e}")


    clear_database()
    
if __name__ == "__main__":
    main()