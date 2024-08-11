import sqlite3

def dict_factory(cursor, row):  
    d = {}  
    for idx, col in enumerate(cursor.description):  
        d[col[0]] = row[idx]  
    return d

def return_cursor(db_file_path:str):
    database = sqlite3.connect(db_file_path)
    database.row_factory = dict_factory
    cursor = database.cursor()
    return database, cursor