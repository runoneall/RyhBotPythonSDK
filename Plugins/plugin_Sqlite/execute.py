import sqlite3

database = None


def run_command(cursor, sql: str):
    cursor.execute(sql)
    database.commit()
    return cursor.fetchall()


def create_table(cursor, table_info: dict):
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
    sql += ';'
    run_command(cursor, sql)


def drop_table(cursor, table_name: str):
    table_name = table_name.replace(' ', '_')
    run_command(cursor, f'DROP TABLE IF EXISTS {table_name};')


def insert(cursor, insert_info: str, ):
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
    run_command(cursor, f'INSERT INTO {table_name} ({keys}) VALUES ({values});')


def delete(cursor, table_name: str, condition: str = ''):
    table_name = table_name.replace(' ', '_')
    sql = f'DELETE FROM {table_name} '
    if condition != '':
        sql += f'WHERE {condition}'
    sql += ';'
    run_command(cursor, sql)


def update(cursor, update_info: dict, condition: str = ''):
    sql = str()
    table_name = update_info['name']
    table_name = table_name.replace(' ', '_')
    sql += f'UPDATE {table_name} '
    control = 'SET '
    update_items = update_info['item']
    for item in update_items:
        item_key = list(item.keys())[0]
        control += f'{item_key}='
        item_value = item[item_key]
        control += f'{item_value}, '
    control = control[:-2] + ' '
    sql += control
    if condition != '':
        sql += f'WHERE {condition}'
    sql += ';'
    run_command(cursor, sql)
