from database import DATABASE

class Member:
  def __init__(self, db):
    self.db_connection = db 

  def add_member(self, name, email, address):
    query = 'INSERT INTO members (name, email, address) VALUES (%s, %s, %s)'
    self.db_connection.cursor.execute(query, (name, email, address))
    self.db_connection.db.commit()
    return f'Added Member: {name}, Email: {email}, Address: {address}'
  
  def delete_member(self, member_id):
    query='DELETE FROM members WHERE member_id=%s'
    self.db_connection.cursor.execute(query, (member_id,))
    self.db_connection.db.commmit()
    return f'Deleted Member ID: {member_id}'
  
  def view_member(self, member_id):
    query='SELECT * FROM members WHERE member_id=%s'
    self.db_connection.cursor.execute(query, (member_id, ))
    return self.db_connection.cursor.fetchone()
  

member_1 = Member(DATABASE())
#print(member_1.add_member('Kelly', 'Kelly@gmail.com', '123 st Everett'))
print(member_1.view_member(2))
