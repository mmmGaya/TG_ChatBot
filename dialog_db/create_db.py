import psycopg2 
import os 


host = os.getenv('DB_HOST')
name = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

def connect_to_database():
    conn = psycopg2.connect(
        dbname=name,
        user=user,
        password=password,
        host=host)
    return conn

def create_table(conn):
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS dialog (
            id SERIAL PRIMARY KEY,
            user_name TEXT,
            user TEXT,
            assistant TEXT)''')
    conn.commit()
    cur.close()

def insert_data(conn, data):
    cur = conn.cursor()
    cur.execute('''INSERT INTO dialog (user_name, user, assistant) VALUES (%s, %s, %s)''', data)
    conn.commit()
    cur.close()





