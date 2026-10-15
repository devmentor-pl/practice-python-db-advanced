from models import Base, Author, Book
from db import engine, Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session() as session:
    try:

        author_1 = Author(name="Daniel Kahneman")
        author_2 = Author(name="Tony Robbins")
        
        book_1 = Book(title="Pułapki myślenia. O myśleniu szybkim i wolnym", author = author_1)
        book_2 = Book(title="Obudź w sobie olbrzyma", author=author_2)
        book_3 = Book(title="Money. Mistrzowska gra", author=author_2)
        book_4 = Book(title="Nasza moc bez granic", author=author_2)
        book_5 = Book(title="Szum", author = author_1)
        
        session.add_all([author_1, author_2, book_1, book_2, book_3, book_4, book_5])

        session.commit()
        
        robbins = session.query(Author).filter(Author.name == "Tony Robbins").first()
        
        if robbins:
            for book in robbins.books:
                print(book.title)  
        else:
            print("Nie znaleziono!")
            
        author_list = session.query(Author).join(Book).group_by(Author.id).having(func.count(Book.id) > 1).all()
        
        if author_list:
            for element in author_list:
                print(element.name)
        else:
            print("Nie znaleziono!")
      
    except SQLAlchemyError as e:
        
        session.rollback()
        print(f"Błąd: {e}")
