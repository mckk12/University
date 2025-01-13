import unittest
"""
Unit tests for the Book and Friend models using SQLAlchemy and an in-memory SQLite database.
Classes:
    TestBooks: Contains unit tests for the Book model.
    TestFriends: Contains unit tests for the Friend model.
TestBooks Methods:
    test_add_book: Tests adding a book to the database.
    test_validate_year: Tests that adding a book with a future year raises a ValueError.
    test_remove_book: Tests removing a book from the database.
TestFriends Methods:
    test_add_friend: Tests adding a friend to the database.
    test_validate_email: Tests that adding a friend with an invalid email raises a ValueError.
    test_remove_friend: Tests removing a friend from the database.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db import Book, Friend, Base


class TestBooks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create an in-memory SQLite database for testing
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)

    def setUp(self):
        # Create a new session for each test
        self.session = Session(self.engine)

    def tearDown(self):
        # Close the session after each test
        self.session.close()

    def test_add_book(self):
        # Test adding a book to the database
        book = Book(title="Test Book", author_name="Author", year=2020)
        self.session.add(book)
        self.session.commit()

        # Verify the book was added
        result = self.session.query(Book).filter_by(title="Test Book").first()
        self.assertIsNotNone(result)
        self.assertEqual(result.author_name, "Author")

    def test_validate_year(self):
        # Test that adding a book with a future year raises a ValueError
        with self.assertRaises(ValueError):
            book = Book(title="Future Book", author_name="Author", year=2025)
            self.session.add(book)

    def test_remove_book(self):
        # Test removing a book from the database
        book = Book(title="Book to Remove", author_name="Author", year=2020)
        self.session.add(book)
        self.session.commit()

        # Remove the book
        self.session.delete(book)
        self.session.commit()

        # Verify the book was removed
        result = self.session.query(Book).filter_by(
            title="Book to Remove").first()
        self.assertIsNone(result)


class TestFriends(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create an in-memory SQLite database for testing
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)

    def setUp(self):
        # Create a new session for each test
        self.session = Session(self.engine)

    def tearDown(self):
        # Close the session after each test
        self.session.close()

    def test_add_friend(self):
        # Test adding a friend to the database
        friend = Friend(name="Test Friend", email="friend@example.com")
        self.session.add(friend)
        self.session.commit()

        # Verify the friend was added
        result = self.session.query(Friend).filter_by(
            name="Test Friend").first()
        self.assertIsNotNone(result)
        self.assertEqual(result.email, "friend@example.com")

    def test_validate_email(self):
        # Test that adding a friend with an invalid email raises a ValueError
        with self.assertRaises(ValueError):
            friend = Friend(name="Invalid Friend", email="invalid-email")
            self.session.add(friend)

    def test_remove_friend(self):
        # Test removing a friend from the database
        friend = Friend(name="Friend to Remove", email="remove@example.com")
        self.session.add(friend)
        self.session.commit()

        # Remove the friend
        self.session.delete(friend)
        self.session.commit()

        # Verify the friend was removed
        result = self.session.query(Friend).filter_by(
            name="Friend to Remove").first()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

