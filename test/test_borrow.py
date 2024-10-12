import sys 
import unittest
import pytest 
from unittest.mock import MagicMock, patch

sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Database/Library-Managment-OOP-MySQL/')

from borrow import Borrow
from database import DATABASE 

class Test_Borrow(unittest.TestCase):

  @patch('mysql.connector.connect')
  def setUp(self, mock_connect): # Set up test run at the beggining of each test
    # Mock db and cursor 
    self.mock_db = MagicMock()
    self.mock_cursor = MagicMock()

    mock_connect.return_value = self.mock_db
    self.mock_db.cursor.return_value = self.mock_cursor

    # Initialize DB 
    self.borrow_1 = Borrow(DATABASE())

  def test_borrow_book(self):
    member_id = 101 # Assume member id is 101 
    book_ids = [1, 2] # Assume list of book_ids is 1, 2 (We have 2 book in the store)

    # Mock Behavior for fetching book stock 
    self.mock_cursor.fetchone.side_effect=[
      (5,), # Book id = 1 
      (3,), # Book id = 2 
 
    ]

    # Call the method want to test 
    self.borrow_1.borrow_book(member_id, book_ids)

    # Assert Query Select book stock 
    self.mock_cursor.execute.assert_any_call(
      'SELECT stock FROM books WHERE book_id=%s',
      (1,)
    )
    self.mock_cursor.execute.assert_any_call(
      'SELECT stock FROM books WHERE book_id=%s',
      (2,)
    )
    

    # Assert Query Insert borrows table 
    self.mock_cursor.execute.assert_any_call(
      'INSERT INTO borrows(member_id, book_id) VALUES(%s, %s)',
      (member_id, 1)
    )
    self.mock_cursor.execute.assert_any_call(
      'INSERT INTO borrows(member_id, book_id) VALUES(%s, %s)',
      (member_id, 2)
    )

    # Assert Query Update book stock 
    self.mock_cursor.execute.assert_any_call(
      'UPDATE books SET stock=%s WHERE book_id=%s',
      (4, 1) # book_id = 1 have 5 - 1 stock
    )
    self.mock_cursor.execute.assert_any_call(
      'UPDATE books SET stock=%s WHERE book_id=%s',
      (2, 2) # book_id = 2 have 3 - 1 stock 
    )

    # Commit assert
    self.mock_db.commit.assert_called_once()


  def test_return_book(self):
    # Alway call fetchone side_effect before call actual method 
    self.mock_cursor.fetchone.side_effect=[(5,)]

    # Call method want to test 
    self.borrow_1.return_book(1)

    

    # Assert Update return date
    self.mock_cursor.execute.assert_any_call(
      'UPDATE borrows SET return_date=CURRENT_TIMESTAMP WHERE book_id=%s',
      (1, )
    )
    # Assert Select stock from book
    self.mock_cursor.execute.assert_any_call(
      'SELECT stock FROM books WHERE book_id=%s',
      (1,)
    )

    # Assert Update book stock 
    #self.mock_cursor.execute.assert_any_call(
     # 'UPDATE books SET stock=%s WHERE book_id=%s',
      #(self.mock_cursor.fetchone().__getitem__().__add__(), 1)
    #)

    self.mock_cursor.execute.assert_any_call(
      'UPDATE books SET stock=%s WHERE book_id=%s',
      (6, 1)
    )

    # Commit 
    self.mock_db.commit.assert_called_once()    




    