from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped, validates
from typing import List

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
    