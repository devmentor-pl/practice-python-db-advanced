from db import Session, engine
from models import Base, Author, Book
from sqlalchemy import func

Base.metadata.create_all(engine)
session = Session()

# 1. Dodaj dwóch autorów i kilka książek przypisanych do każdego.
author1 = Author(name="Andrzej Sapkowski")
author2 = Author(name="Jarosław Grzędowicz")
book1 = Book(title="Saga o Wiedźminie", author_id=1)
book2 = Book(title="Pan lodowego ogrodu", author_id=2)
book3 = Book(title="Popiół i kurz", author_id=2)
book4 = Book(title="Hel-3", author_id=2)

session.add_all([author1, author2, book1, book2, book3, book4])
session.commit()

# 2. Pobierz i wypisz wszystkie książki konkretnego autora (np. „Jan Nowak”).
books_author1 = session.query(Book).join(Book.author).filter(Author.name == "Andrzej Sapkowski").all()
print("Lista książek Andrzeja Sapkowskiego:")
for book in books_author1:
    print(book.title)

# 3. Pobierz listę autorów, którzy mają więcej niż jedną książkę.
author_manybooks = session.query(Author).join(Author.book).group_by(Author.id).having(func.count(Book.id) > 1).all()
print("\nAutorzy mający więcej niż 1 wydaną książkę:")
for author in author_manybooks:
    print(author.name)

session.close()