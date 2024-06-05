import sqlite3
import random
import uuid
from datetime import date


#USER----TABLE
def createTables():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id VARCHAR(255),
            password VARCHAR(255),
            level INT,
            dateOfAccountCreation DATE,
            approved BOOLEAN,
            blocked BOOLEAN,
            name VARCHAR(255),
            address VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(255),
            pinCode VARCHAR(255)
        );
 ''')



#PRODUCT-----TABLE

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            price FLOAT,
            category VARCHAR(255),
            stock INT,
            isActive BOOLEAN
     );
''')







  #Create Order table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders(
            orderId INTEGER PRIMARY KEY AUTOINCREMENT,
            quantity VARCHAR(255),
            dateOfOrderCreation DATE,
            ProductId INT,
            venderId VARCHAR(255)
        );
    ''')
    conn.commit()
    conn.close()



 #CREATE--------------USER

def createUser(name,password,phone,email, address, pinCode):
    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    user_id= str(uuid.uuid4())
    dateOfCreation = date.today()
    conn.execute("""
INSERT INTO User (user_id, password, level, dateOfAccountCreation, approved, blocked, name, address, email, phone, pinCode)
 VALUES
     (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", (user_id,password,-1, dateOfCreation, 0,0,name, address,email,phone,pinCode))
    conn.commit()
    conn.close()
    return True





#CREATE----Order


def createOrder(quantity):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    dateOfOrderCreation = date.today()
    cursor.execute("""
        INSERT INTO Orders (quantity, dateOfOrderCreation)
        VALUES (?, ? );
    """, (quantity,dateOfOrderCreation))

    conn.commit()
    conn.close()
    return True













