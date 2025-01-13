"""
This module implements a Flask web server for managing books, friends, and loans.
Routes:
    / (GET): Main page route.
    /books (GET): List all books.
    /books (PUT): Add a new book.
    /books/<int:book_id> (DELETE): Remove a book by ID.
    /books/<int:book_id> (POST): Edit a book by ID.
    /friends (GET): List all friends.
    /loans (GET): List all loans.
Configuration:
    DATABASE: The database connection string for SQLAlchemy.
Dependencies:
    Flask: A micro web framework for Python.
    SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
    db: A module containing the Book, Loan, and Friend ORM models.
"""

from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db import Book, Loan, Friend

app = Flask(__name__)
app.config['DATABASE'] = 'postgresql://postgres:pass@localhost:5432/testbase'

engine = create_engine(app.config['DATABASE'])
session = Session(engine)


@app.route("/")
def main():
    # Main page route
    return "<p>Main page</p>"


@app.route('/books', methods=['GET'])
def list_books():
    # List all books
    books = session.query(Book).all()
    return jsonify([{'id': book.id, 'title': book.title,
                   'author': book.author_name, 'year': book.year} for book in books])


@app.route('/books', methods=['PUT'])
def add_book():
    # Add a new book
    data = request.json
    book = Book(
        title=data['title'],
        author_name=data['author'],
        year=data['year'])
    session.add(book)
    session.commit()
    return jsonify({'id': book.id, 'title': book.title,
                   'author': book.author_name, 'year': book.year})


@app.route('/books/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    # Remove a book by ID
    book = session.query(Book).get(book_id)
    session.delete(book)
    session.commit()
    return jsonify({'id': book.id, 'title': book.title,
                   'author': book.author_name, 'year': book.year})


@app.route('/books/<int:book_id>', methods=['POST'])
def edit_book(book_id):
    # Edit a book by ID
    data = request.json
    book = session.query(Book).get(book_id)
    book.title = data['title']
    book.author_name = data['author']
    book.year = data['year']
    session.commit()
    return jsonify({'id': book.id, 'title': book.title,
                   'author': book.author_name, 'year': book.year})


@app.route('/friends', methods=['GET'])
def list_friends():
    # List all friends
    friends = session.query(Friend).all()
    return jsonify([{'id': friend.id, 'name': friend.name,
                   'email': friend.email} for friend in friends])


@app.route('/loans', methods=['GET'])
def list_loans():
    # List all loans
    loans = session.query(Loan).all()
    return jsonify([{'id': loan.id, 'book_id': loan.book_id,
                   'friend_id': loan.friend_id} for loan in loans])
