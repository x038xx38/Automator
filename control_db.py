import sqlite3
from sqlite3 import Error


def create_connection(file):
    conn = None
    try:
        conn = sqlite3.connect(file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


def create_database(file):
    sql_offers_table = """ CREATE TABLE IF NOT EXISTS goods (
                            id integer PRIMARY KEY,
                            modified_time text NOT NULL,
                            categoryId text NOT NULL,
                            vendor text NOT NULL,
                            name text NOT NULL,
                            description text NOT NULL,
                            param text NOT NULL,
                            picture text NOT NULL,
                            oldprice text NOT NULL,
                            price text NOT NULL,
                            url text NOT NULL
                        ); """

    conn = create_connection(file)
    if conn is not None:
        create_table(conn, sql_offers_table)
    else:
        print('Ошибка! Не получается создать подключение к Базе данных!')


def add_offer(conn, row):
    sql = """INSERT INTO goods(modified_time, categoryId, vendor, name, description, param, picture, oldprice, price,
            url) VALUES(?,?,?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, row)
    conn.commit()
    return cur.lastrowid


if __name__ == '__main__':
    # database = r'database.db'
    # create_database(database)
    pass