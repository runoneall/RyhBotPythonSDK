import sqlite3

database = None

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
    cursor.execute(sql)
    database.commit()

def drop_table(cursor, table_name:str):
    table_name = table_name.replace(' ', '_')
    cursor.execute(f'DROP TABLE IF EXISTS {table_name};')
    database.commit()

