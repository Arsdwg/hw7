import sqlite3

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def insert(connection, product):
    sql = '''INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete(connection, idi):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (idi,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_quantity(connection, idi, quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (quantity, idi,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(connection, idi, price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (price, idi,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def createtable(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def printall(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def sortf(connection):
    sql = '''SELECT * FROM products WHERE price <= 100 AND quantity >= 5'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def searchname(connection, name):

    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM products WHERE name LIKE ? ''', ('%' + name + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create = ('CREATE TABLE products ('
                 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                 'name VARCHAR(200) NOT NULL,price FLOAT(8,2) NOT NULL DEFAULT 0.0,'
                 'quantity INTEGER NOT NULL DEFAULT 0)')


myconnection = create_connection('hw.db')
# products1 = [
#     ("banana", 100, 3),
#     ("kirieshki", 20, 20),
#     ("moloko", 20, 20),
#     ("apple", 208, 20),
#     ("potato", 280, 20),
#     ("orange", 270, 20),
#     ("samsa", 20, 20),
#     ("candy", 207, 20),
#     ("iphone", 2660, 20),
#     ("samsung", 270, 20),
#     ("tesla", 205, 20),
#     ("jam jar", 230, 20),
#     ("ilims", 204, 20),
#     ("game", 23, 20),
#     ("shampoo", 10, 20),
#     ("imarat", 20, 20),
# ]
# for product in products1:
#     insert(myconnection, product)
update_quantity(myconnection, 7, 100)
update_price(myconnection, 7, 100)


# createtable(myconnection, sql_to_create)
# insert(myconnection, ('banana', 100, 1))
# delete(myconnection, 0)
# printall(myconnection)
# sortf(myconnection)
searchname(myconnection, 'tesla')
myconnection.close()
