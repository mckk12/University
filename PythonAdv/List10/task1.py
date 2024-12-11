from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, mapped_column, Mapped, Session, validates
from sqlalchemy import create_engine
import argparse
import json
from typing import List

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'Books'
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String)
    author_name = mapped_column(String)
    year = mapped_column(Integer)

    friend_id = mapped_column(Integer, ForeignKey('Friends.id'))
    friend = relationship('Friend', back_populates='borrowed_books')


    @validates('year')
    def validate_year(self, key, value):
        if value > 2024:
            raise ValueError("The book can't be from the future!")
        return value

class Friend(Base):
    __tablename__ = 'Friends'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    email = mapped_column(String)

    borrowed_books: Mapped[List[Book]] = relationship('Book', back_populates='friend')

    @validates('email')
    def validate_email(self, key, value):
        if '@' not in value:
            raise ValueError("Invalid email address")
        return value
    

def init_db(json_file, engine, session):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with open(json_file, 'r') as file:
        data = json.load(file)
        for friend in data['friends']:
            session.add(Friend(**friend))
            
        for book in data['books']:
            session.add(Book(**book))

        session.commit()

def add_book(session, title, author_name, year):
    session.add(Book(title=title, author_name=author_name, year=year))
    session.commit()
    print(f'Book {title} added')

def remove_book(session, book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    session.delete(book)
    session.commit()
    print(f'Book {book.title} removed')

def edit_book(session, book_id, title, author_name, year):
    book = session.query(Book).filter(Book.id == book_id).first()
    book.title = title
    book.author_name = author_name
    book.year = year
    session.commit()
    print(f'Book {book.title} edited')

def add_friend(session, name, email):
    session.add(Friend(name=name, email=email))
    session.commit()
    print(f'Friend {name} added')

def remove_friend(session, friend_id):
    friend = session.query(Friend).filter(Friend.id == friend_id).first()
    session.delete(friend)
    session.commit()
    print(f'Friend {friend.name} removed')

def edit_friend(session, friend_id, name, email):
    friend = session.query(Friend).filter(Friend.id == friend_id).first()
    friend.name = name
    friend.email = email
    session.commit()
    print(f'Friend {friend.name} edited')

def borrow_book(session, book_id, friend_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    friend = session.query(Friend).filter(Friend.id == friend_id).first()
    book.friend = friend
    friend.borrowed_books.append(book)
    session.commit()
    print(f'Book {book.title} borrowed by {friend.name}')

def return_book(session, book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    friend = book.friend
    book.friend = None
    friend.borrowed_books.remove(book)
    session.commit()
    print(f'Book {book.title} returned by {friend.name}')

def list_books(session):
    books = session.query(Book).all()
    for book in books:
        status = 'borrowed' if book.friend else 'available'
        print(f'{book.id} {book.title} {book.author_name} {book.year} - {status}')

def list_friends(session):
    friends = session.query(Friend).all()
    for friend in friends:
        print(f'{friend.name} {friend.email}')
    


parser = argparse.ArgumentParser(description='Book lending system')
parser.add_argument('--init-db', action="store_true", help='Initialize the database')

subparsers = parser.add_subparsers(dest='command')

books_parser = subparsers.add_parser('books')
books_parser.add_argument('--list', action='store_true', help='List all books')
books_parser.add_argument('--add', nargs=3, metavar=('title', 'author_name', 'year'), help='Add a new book')
books_parser.add_argument('--remove', metavar='book_id', help='Remove a book')
books_parser.add_argument('--edit', nargs=4, metavar=('book_id', 'title', 'author_name', 'year'), help='Edit a book')
books_parser.add_argument('--borrow', nargs=2, metavar=('book_id', 'friend_id'), help='Borrow a book')
books_parser.add_argument('--returning', metavar='book_id', help='Return a borrowed book')

friends_parser = subparsers.add_parser('friends')
friends_parser.add_argument('--list', action='store_true', help='List all friends')
friends_parser.add_argument('--add', nargs=2, metavar=('name', 'email'), help='Add a new friend')
friends_parser.add_argument('--remove', metavar='friend_id', help='Remove a friend')
friends_parser.add_argument('--edit', nargs=3, metavar=('friend_id', 'name', 'email'), help='Edit a friend')


engine = create_engine('postgresql://postgres:pass@localhost:5432/testbase') #echo=True if you want to see the SQL logs
session = Session(engine)


args = parser.parse_args()


if args.init_db:
    init_db('library.json', engine, session)
elif args.command == 'books':
    if args.list:
        list_books(session)
    elif args.add:
        add_book(session, *args.add)
    elif args.borrow:
        borrow_book(session, *args.borrow)
    elif args.returning:
        return_book(session, args.returning)
elif args.command == 'friends':
    if args.list:
        list_friends(session)
    elif args.add:
        add_friend(session, *args.add)
session.close()


