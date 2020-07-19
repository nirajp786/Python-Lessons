import psycopg2

connection_details = "dbname='database 1' user='postgres' password='159753123PG' host='localhost' port='5432'"

def create_table():
    try:
        connection = psycopg2.connect(connection_details)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
        connection.commit()
        connection.close()
    except Exception as e:
        print("Can't connect. Invalid dbname, user or password")
        print(e)
        
def insert(item, quantity, price):
    try:
        connection = psycopg2.connect(connection_details)
        cursor = connection.cursor()
        #cursor.execute("INSERT INTO store VALUES('%s', '%s', '%s')" % (item, quantity, price))
        cursor.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
        connection.commit()
        connection.close()
    except Exception as e:
        print("Insert was not done")
        print(e)
        
def view():
    try:
        connection = psycopg2.connect(connection_details)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM store")
        rows = cursor.fetchall()
        connection.close()
        return rows
    except Exception as e:
        print("Cannot view the rows")
        return e

def delete(item):
    try:
        connection = psycopg2.connect(connection_details)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM store WHERE store.item=%s", (item,))
        connection.commit()
        connection.close()
    except Exception as e:
        print("Delete operation was not done")
        print(e)

def update(item, quantity, price):
    try:
        connection = psycopg2.connect(connection_details)
        cursor = connection.cursor()
        cursor.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
        connection.commit()
        connection.close()
    except Exception as e:
        print("Update operation was not done")
        print(e)

create_table()
#insert("Grape", 2, 2.5)
print(view())
update("Orange", 2, 4)
print(view())