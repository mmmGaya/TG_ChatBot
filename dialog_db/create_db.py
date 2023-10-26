import psycopg2 
import os 
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_HOST')
name = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

def connect_to_database():
    global conn, cur
    conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=name)
    cur = conn.cursor()
    if conn:
        print('DataBase connected')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS dialog (
            id SERIAL PRIMARY KEY,
            person_name TEXT,
            person TEXT,
            assistant TEXT)''')
    conn.commit()
   

async def insert_data(data):
    cur.execute('''INSERT INTO dialog (person_name, person, assistant) VALUES (%s, %s, %s)''', data)
    conn.commit()
   





