'''
  Book Management:
  Add new books, assign multiple authors to a book.
  Update book details (title, description, stock).
  Manage many-to-many relationship with authors.
'''
from database import DATABASE

class Book:
  def __init__(self, db):
    self.db_connection = db 
  
  def add_new_book(self, title, description, stock, author_ids):
    query='INSERT INTO books (title, description, stock) VALUES (%s, %s, %s)'
    self.db_connection.cursor.execute(query, (title, description, stock))
    book_id = self.db_connection.cursor.lastrowid

    # Link authors to the book
    for author_id in author_ids:
      query_link = 'INSERT INTO book_authors (book_id, author_id) VALUES (%s, %s)'
      self.db_connection.cursor.execute(query_link, (book_id, author_id))

    self.db_connection.db.commit()
    return f'Added Book {title} , AuthorId: {author_id}'
  
  def delete_book(self, book_id):
    # Delete Book authors relationship first
    link_query='DELETE FROM book_authors WHERE book_id=%s'
    self.db_connection.cursor.execute(link_query, (book_id,))

    # Delete the book 
    query = 'DELETE FROM books WHERE book_id=%s'
    self.db_connection.cursor.execute(query, (book_id,))

    self.db_connection.db.commit()

    return f'Deleted bookID: {book_id}'
  
  def view_book(self, book_id):
    query='SELECT * from books WHERE book_id=%s'
    self.db_connection.cursor.execute(query, (book_id, ))
    return (self.db_connection.cursor.fetchone())

book_1 = Book(DATABASE())
book_1.delete_book(1)




  