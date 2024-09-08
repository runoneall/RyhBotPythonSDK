import pymysql

def connect(host:str, user:str, password:str, database:str, port:int=3306):
    database = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset='utf8'
    )
    cursor = database.cursor(pymysql.cursors.DictCursor)
    return database, cursor

def disconnect(database, cursor):
    cursor.close()
    database.close()