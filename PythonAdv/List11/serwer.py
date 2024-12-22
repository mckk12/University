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
    return "<p>Main page</p>"

@app.route('/books', methods=['GET'])
def list_books():
    books = session.query(Book).all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author_name, 'year': book.year} for book in books])

@app.route('/books', methods=['PUT'])
def add_book():
    data = request.json
    book = Book(title=data['title'], author_name=data['author'], year=data['year'])
    session.add(book)
    session.commit()
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author_name, 'year': book.year})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    book = session.query(Book).get(book_id)
    session.delete(book)
    session.commit()
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author_name, 'year': book.year})

@app.route('/books/<int:book_id>', methods=['POST'])
def edit_book(book_id):
    data = request.json
    book = session.query(Book).get(book_id)
    book.title = data['title']
    book.author_name = data['author']
    book.year = data['year']
    session.commit()
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author_name, 'year': book.year})
    
@app.route('/friends', methods=['GET'])
def list_friends():
    friends = session.query(Friend).all()
    return jsonify([{'id': friend.id, 'name': friend.name, 'email': friend.email} for friend in friends])

@app.route('/loans', methods=['GET'])
def list_loans():
    loans = session.query(Loan).all()
    return jsonify([{'id': loan.id, 'book_id': loan.book_id, 'friend_id': loan.friend_id} for loan in loans])