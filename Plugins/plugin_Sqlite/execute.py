import sqlite3

database = None

def create_table(cursor, sql):
    cursor.execute(sql)
    database.commit()