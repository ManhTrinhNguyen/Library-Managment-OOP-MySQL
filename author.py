from database import DATABASE

# Add, Update, View, Delete Author 

class Author:
  def __init__(self, db):
    self.db_connection = db # Connect Database 
  
  def add_author(self, name, bio):
    query='INSERT INTO authors (name, bio) VALUES (%s, %s)'
    self.db_connection.cursor.execute(query, (name, bio))
    self.db_connection.db.commit()
    return f'Added Author: {name}, Bio: {bio}'

  def update_author_name(self, author_id, name):
    # Name before Updated 
    select_query='SELECT name FROM authors WHERE author_id=%s'
    self.db_connection.cursor.execute(select_query, (author_id,))
    name_before_update = self.db_connection.cursor.fetchone()[0]
    
    # Name after Updated 
    update_query='UPDATE authors SET name=%s WHERE author_id=%s'
    self.db_connection.cursor.execute(update_query, (name, author_id,))
    self.db_connection.db.commit()
    return f'Updated Author name from {name_before_update} to {name}'
  
  def update_author_bio(self, author_id, bio):
    # Bio before Updated 
    select_query='SELECT bio FROM authors WHERE author_id=%s'
    self.db_connection.cursor.execute(select_query, (author_id,))
    bio_before_update = self.db_connection.cursor.fetchone()[0]
    
    # Name after Updated 
    update_query='UPDATE authors SET bio=%s WHERE author_id=%s'
    self.db_connection.cursor.execute(update_query, (bio, author_id,))
    self.db_connection.db.commit()
    return f'Updated Author bio from {bio_before_update} to {bio}'
  
  def delete_author(self, author_id):
    delete_query ='DELETE FROM authors WHERE author_id=%s'
    self.db_connection.cursor.execute(delete_query, (author_id,))
    self.db_connection.db.commit()
    return f'Deleted author with id {author_id}'
  
  def view_author(self, author_id):
    query='SELECT * from authors WHERE author_id=%s'
    self.db_connection.cursor.execute(query, (author_id, ))
    print(self.db_connection.cursor.fetchone())


# author_1 = Author(DATABASE())

# print(author_1.view_author())

    
  