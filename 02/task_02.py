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


class Author(Base):

    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author')


class Book(Base):

    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')


Base.metadata.create_all(engine)

author_1 = Author(name='Autor pierwszy')
author_2 = Author(name='Autor drugi')

book_1 = Book(title='title1', author=author_1)
book_2 = Book(title='tytuł2', author=author_1)
book_3 = Book(title='tytuł3', author=author_2)

session.add_all([author_1, author_2, book_1, book_2, book_3])
session.commit()

books_author1 = session.query(Book).filter_by(author=author_1).all()

author_with_books = session.query(Author).join(Book).group_by(
    Author.id).having(func.count(Book.id) > 1).all()

for author in author_with_books:
    print(author.name)

session.close()
