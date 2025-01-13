from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped, validates
from typing import List

class Base(DeclarativeBase):
    pass

class Book(Base):
    """
    Represents a book in the library.
    Attributes:
        id (int): The primary key of the book.
        title (str): The title of the book.
        author_name (str): The name of the author of the book.
        year (int): The year the book was published.
        loan_info (List[Loan]): The list of loans associated with the book.
    Methods:
        validate_year(key, value):
            Validates the year to ensure it is not in the future.
    """
    __tablename__ = 'Books'
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String)
    author_name = mapped_column(String)
    year = mapped_column(Integer)

    loan_info = relationship('Loan', back_populates='book')

    @validates('year')
    def validate_year(self, key, value):
        if value > 2024:
            raise ValueError("The book can't be from the future!")
        return value

class Loan(Base):
    """
    Represents a loan of a book to a friend.
    Attributes:
        id (int): The primary key of the loan.
        date (datetime): The date when the loan was made.
        book_id (int): The foreign key referencing the book being loaned.
        friend_id (int): The foreign key referencing the friend who borrowed the book.
        book (Book): The relationship to the Book model.
        friend (Friend): The relationship to the Friend model.
    Methods:
        validate_friendid(key, value):
            Validates the friend_id to ensure it is not negative.
    """
    __tablename__ = 'Loans'
    id = mapped_column(Integer, primary_key=True)
    date = mapped_column(DateTime)

    book_id = mapped_column(Integer, ForeignKey('Books.id'))
    friend_id = mapped_column(Integer, ForeignKey('Friends.id'))
    book = relationship('Book', back_populates='loan_info')
    friend = relationship('Friend', back_populates='loans')

    @validates('friend_id')
    def validate_friendid(self, key, value):
        if value < 0:
            raise ValueError("Invalid friend id")
        return value

class Friend(Base):
    """
    Represents a friend who can borrow books.
    Attributes:
        id (int): The primary key of the friend.
        name (str): The name of the friend.
        email (str): The email address of the friend.
        loans (List[Loan]): The list of loans associated with the friend.
    Methods:
        validate_email(key, value):
            Validates the email to ensure it contains an '@' symbol.
    """
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
