import sys
import unittest
from unittest.mock import patch, MagicMock
import unittest.mock
import pytest
sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Database/Library-Managment-OOP-MySQL/')

from database import DATABASE
from book import Book

class TestBook(unittest.TestCase):

  @patch('mysql.connector.connect') # Pass mock mysql.connector as the arg 
  def setUp(self, mock_connect): # setUp method run at the beginning of each test
    # Mock connect db 
    self.mock_db = MagicMock()
    # Mock connect cursor 
    self.mock_cursor = MagicMock()

    # Mock_connect (mysql.connector.connect) will return value as mock_db
    mock_connect.return_value = self.mock_db
    # Mock_db.cursor will return self._mock_cursor 
    self.mock_db.cursor.return_value = self.mock_cursor

    # Initilize DB 
    self.book=Book(DATABASE())

  def test_add_new_book(self):
    # I have 2 authors
    author_ids = [1, 2]

    # Mock lastrowid 
    self.mock_cursor.lastrowid = 101 # Assume lastrowid is 101

    # Call Method want to test
    self.book.add_new_book('One Thing', 'Self-help', 10, author_ids)

    # Assert call insert book
    self.mock_cursor.execute.assert_any_call(
      'INSERT INTO books (title, description, stock) VALUES (%s, %s, %s)',
      ('One Thing', 'Self-help', 10)
    )
    # Assert call insert book_author
    for author_id in author_ids:
      self.mock_cursor.execute.assert_any_call(
        'INSERT INTO book_authors (book_id, author_id) VALUES (%s, %s)',
        (101, author_id)  # 101 is the mocked book_id
      )

    self.mock_db.commit.assert_called_once()

  def test_delete_book(self):
    # call method want to test
    self.book.delete_book(1)
    
    # Assert delete from book_authors
    self.mock_cursor.execute.assert_any_call(
      'DELETE FROM book_authors WHERE book_id=%s',
      (1,)
    )
    # Assert delete from books
    self.mock_cursor.execute.assert_any_call(
      'DELETE FROM books WHERE book_id=%s',
      (1,)
    )

    self.mock_db.commit.assert_called_once()

  def test_view_book(self):
    # Call method want to test 
    self.book.view_book(1)

    # Assert select book 
    # Select query don't need commit
    self.mock_cursor.execute.assert_any_call(
      'SELECT * from books WHERE book_id=%s',
      (1,)
    )
    

    
