import psycopg2 
import os 


host = os.getenv('DB_HOST')
name = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

def connect_to_database():
    global conn, cur
    conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='qwerty',
            database='dialog')
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
   





