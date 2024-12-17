from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped, Session, validates
from sqlalchemy import create_engine
import argparse
import json
from typing import List
import datetime

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'Books'
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String)
    author_name = mapped_column(String)
    year = mapped_column(Integer)

    # loan_id = mapped_column(Integer, ForeignKey('Loans.id'))
    loan_info = relationship('Loan', back_populates='book')


    @validates('year')
    def validate_year(self, key, value):
        if value > 2024:
            raise ValueError("The book can't be from the future!")
        return value
    
class Loan(Base):
    __tablename__ = 'Loans'
    id = mapped_column(Integer, primary_key=True)
    date = mapped_column(DateTime)

    book_id = mapped_column(Integer, ForeignKey('Books.id'))
    friend_id = mapped_column(Integer, ForeignKey('Friends.id'))
    book = relationship('Book', back_populates='loan_info')
    friend = relationship('Friend', back_populates='loans')

    @validates
    def validate_friendid(self, key, value):
        if value < 0:
            raise ValueError("Invalid friend id")
        return value
    
class Friend(Base):
    __tablename__ = 'Friends'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    email = mapped_column(String)

    loans: Mapped[List[Loan]] = relationship('Loan', back_populates='friend')

    @validates('email')
    def validate_email(self, key, value):
        if '@' not in value:
            raise ValueError("Invalid email address")
        return value
    

#functions for initializing the database
def init_db(json_file, engine, session):
    # Base.metadata.drop_all(engine, checkfirst=True)
    Base.metadata.create_all(engine)

    with open(json_file, 'r') as file:
        data = json.load(file)
        for friend in data['friends']:
            session.add(Friend(**friend))
            
        for book in data['books']:
            session.add(Book(**book))

        session.commit()


#functions for books
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

def list_books(session):
    books = session.query(Book).all()
    for book in books:
        status = 'borrowed' if book.loan_id else 'available'
        print(f'{book.id} {book.title} {book.author_name} {book.year} - {status}')    


#functions for friends
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

def list_friends(session):
    friends = session.query(Friend).all()
    for friend in friends:
        print(f'{friend.name} {friend.email}')
    

#functions for loans
def add_loan(session, book_id, friend_id):
    current_date = datetime.now()
    loan = Loan(date=current_date, book_id=book_id, friend_id=friend_id)
    session.add(loan)
    session.commit()
    print(f'Book {loan.book.title} borrowed by {loan.friend.name}')

def remove_loan(session, loan_id):
    loan = session.query(Loan).filter(Loan.id == loan_id).first()
    friend = loan.friend
    friend.loans.remove(loan)
    book = loan.book
    # book.loan_id = None
    session.delete(loan)
    session.commit()
    print(f'Loan {loan.id} removed')

def list_loans(session):
    loans = session.query(Loan).all()
    for loan in loans:
        print(f'{loan.id} {loan.book.title} borrowed by {loan.friend.name} on {loan.date}')



parser = argparse.ArgumentParser(description='Book lending system')
parser.add_argument('--init-db', action="store_true", help='Initialize the database')
subparsers = parser.add_subparsers(dest='table')


books_parser = subparsers.add_parser('books')
books_parser.add_argument('--list', action='store_true', help='List all books')
books_parser.add_argument('--add', action='store_true', help='Add a new book')
books_parser.add_argument('--remove', metavar='book_id', help='Remove a book')
books_parser.add_argument('--edit', action='store_true', help='Edit a book')
books_parser.add_argument('--book_id', type=int, help='ID of the book')
books_parser.add_argument('--title', type=str, help='Title of the book')
books_parser.add_argument('--author_name', type=str, help='Author of the book')
books_parser.add_argument('--year', type=int, help='Year of the book')


friends_parser = subparsers.add_parser('friends')
friends_parser.add_argument('--list', action='store_true', help='List all friends')
friends_parser.add_argument('--add', action='store_true', help='Add a new friend')
friends_parser.add_argument('--remove', action='store_true', help='Remove a friend')
friends_parser.add_argument('--edit', action='store_true', help='Edit a friend')
friends_parser.add_argument('--friend_id', type=int, help='ID of the friend')
friends_parser.add_argument('--name', type=str, help='Name of the friend')
friends_parser.add_argument('--email', type=str, help='Email of the friend')

loans_parser = subparsers.add_parser('loans')
loans_parser.add_argument('--list', action='store_true', help='List all loans')
loans_parser.add_argument('--add', action='store_true', help='Add a new loan')
loans_parser.add_argument('--remove', action='store_true', help='Remove a loan')
loans_parser.add_argument('--friend_id', type=int, help='ID of the friend borrowing the book')
loans_parser.add_argument('--book_id', type=int, help='ID of the book being borrowed')


engine = create_engine('postgresql://postgres:pass@localhost:5432/testbase') #echo=True if you want to see the SQL logs
session = Session(engine)
args = parser.parse_args()


if args.init_db:
    init_db('library.json', engine, session)
elif args.table == 'books':
    if args.list:
        list_books(session)
    elif args.add:
        add_book(session, args.title, args.author_name, args.year)
    elif args.remove:
        remove_book(session, args.book_id)
    elif args.edit:
        edit_book(session, args.book_id, args.title, args.author_name, args.year)
elif args.table == 'friends':
    if args.list:
        list_friends(session)
    elif args.add:
        add_friend(session, args.name, args.email)
    elif args.remove:
        remove_friend(session, args.friend_id)
    elif args.edit:
        edit_friend(session, args.friend_id, args.name, args.email)
elif args.table == 'loans':
    if args.list:
        list_loans(session)
    elif args.add:
        add_loan(session, args.book_id, args.friend_id)
    elif args.remove:
        remove_loan(session, args.loan_id)
else:
    parser.print_help()

session.close()


