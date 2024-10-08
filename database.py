import mysql.connector 
from dotenv import load_dotenv
import os 

# Load environment variables from the .env file (if present)
load_dotenv()

class DATABASE:
  def __init__(self):
    self.db = mysql.connector.connect(
      host='localhost',
      user=os.getenv('DB_USER'),
      password=os.getenv('DB_PASSWORD'),
      database='library_2'
    )
    self.cursor = self.db.cursor()


db = DATABASE()
