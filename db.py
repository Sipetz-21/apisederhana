import sqlite3
from sqlite3 import tables


DATABASE_NAME = "db_tekkom_0413.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table():
    tables =[
            """CREATE TABLE IF NOT EXISTS
                tbl_news_0413(
                title TEXT NOT NULL,
                content	TEXT NOT NULL,
                news_id	INTEGER NOT NULL PRIMARY KEY,
                datetime TEXT NOT NULL,
                flag INTEGER NOT NULL""" 
        ]
    
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)
