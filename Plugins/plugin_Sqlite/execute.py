import sqlite3

database = None

def Execute(cursor, sql:str):
    cursor.execute(sql)
    database.commit()
    return cursor.fetchall()

def create_table(cursor, table_info:dict):
    sql = str()
    table_name = table_info['name']
    table_name = table_name.replace(' ', '_')
    sql += f'CREATE TABLE {table_name} ('
    table_items = table_info['item']
    for item in table_items:
        item_key = list(item.keys())[0]
        item_type = item[item_key]
        sql += f'{item_key} {item_type}, '
    sql = sql[:-2] + ')'
    Execute(cursor, sql)

def drop_table(cursor, table_name:str):
    table_name = table_name.replace(' ', '_')
    Execute(cursor, f'DROP TABLE IF EXISTS {table_name};')

def insert(cursor, insert_info:str, ):
    table_name = insert_info['name']
    table_name = table_name.replace(' ', '_')
    insert_items = insert_info['item']
    keys = str()
    values = str()
    for item in insert_items:
        item_key = list(item.keys())[0]
        keys += f'{item_key},'
        item_value = item[item_key]
        values += f'{item_value},'
    keys = keys[:-1]
    values = values[:-1]
    Execute(cursor, f'INSERT INTO {table_name} ({keys}) VALUES ({values});')