import sqlite3

def create_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()
    
    
def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    #cursor.execute("INSERT INTO store VALUES('Wine Glass', 8, 10.5)")
    cursor.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    connection.commit()
    connection.close()

def display_data():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    
    return rows

def delete(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    #deltes the water since water quantity was 10
    #cursor.execute("DELETE FROM store WHERE store.quantity = 10")
    #cursor.execute("DELETE FROM store WHERE item=?", (item,))
    cursor.execute("DELETE FROM store")
    connection.commit()
    connection.close()
    
def update(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity = 69 WHERE item = ?", (item,))
    connection.commit()
    connection.close()

#insert("Water Glass", 10, 5)
#insert("Coffe", 2, 10.3)
#insert("daru", 2, 2)
#insert("Wine", 12, 24)
#insert("Wine Glass", 1, 10)
print(display_data())
#delete("Wine")
update("Wine")
print(display_data())