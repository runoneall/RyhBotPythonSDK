import sqlite3

def return_cursor(db_file_path:str):
    database = sqlite3.connect(db_file_path)
    cursor = database.cursor()
    return database, cursor