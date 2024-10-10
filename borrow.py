from database import DATABASE 

class Borrow: 
  def __init__(self, db):
    self.db_connection = db 

  # Allow member to borrow mutilple books (one to many relationship)
  def borrow_book(self, member_id, book_ids):
    # book_ids should be a list
    # Iterate through book_ids
    for book_id in book_ids:
      # Check if book available 
      query_book_stock='SELECT stock FROM books WHERE book_id=%s'
      self.db_connection.cursor.execute(query_book_stock, (book_id,))
      book_stock = self.db_connection.cursor.fetchone()
      if book_stock and book_stock[0] > 0:
         # Insert into borrows table 
         query_borrow_book='INSERT INTO borrows(member_id, book_id) VALUES(%s, %s)'
         self.db_connection.cursor.execute(query_borrow_book, (member_id, book_id))

         # Reduce stock 
         reduce_stock = book_stock[0] - 1
         query_reduce_stock='UPDATE books SET stock=%s WHERE book_id=%s'
         self.db_connection.cursor.execute(query_reduce_stock,(reduce_stock, book_id))
      else:
        return f'Book with {book_id} is out of stock'
    # Commit Transaction
    self.db_connection.db.commit()
    print(f"Member {member_id} successfully borrowed books: {book_ids}")

  def return_book(self, book_id):
    # Return book 
    query_return='UPDATE borrows SET return_date=CURRENT_TIMESTAMP WHERE book_id=%s'
    self.db_connection.cursor.execute(query_return, (book_id,))

    # Update sock in books
    query_book_stock='SELECT stock FROM books WHERE book_id=%s'
    self.db_connection.cursor.execute(query_book_stock, (book_id,))
    book_stock = self.db_connection.cursor.fetchone()[0]
    new_stock = book_stock + 1
    query_update_book_stock='UPDATE books SET stock=%s WHERE book_id=%s'
    self.db_connection.cursor.execute(query_update_book_stock, (new_stock, book_id))

    self.db_connection.db.commit()

  # Generate a report of the most borrowed book 
  def most_borrowed_book(self):
    query='''
    SELECT books.title, COUNT(borrows.book_id) as borrow_count 
    FROM borrows
    JOIN books ON borrows.book_id = books.book_id
    GROUP BY borrows.book_id
    ORDER BY borrow_count DESC
    '''

    self.db_connection.cursor.execute(query)
    results = self.db_connection.cursor.fetchall()
    print(f'Most borrowed books: {results[0][0]}, Times Borrowed: {results[0][1]}')

  def most_active_member(self):
    query='''
    SELECT members.name, COUNT(borrows.member_id) as member_count
    FROM borrows
    JOIN members ON borrows.member_id = members.member_id
    GROUP BY borrows.member_id
    ORDER BY member_count DESC
    '''
    self.db_connection.cursor.execute(query)
    results=self.db_connection.cursor.fetchall()
    print(f'Most active member: {results[0][0]}')



borrow_1 = Borrow(DATABASE())
# borrow_1.borrow_book(2, [6])
# borrow_1.borrow_book(3, [3,4])
# borrow_1.borrow_book(4, [3,6])
# borrow_1.borrow_book(5, [3,6])
# borrow_1.return_book(3)
borrow_1.most_active_member()
