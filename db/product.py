import sqlite3

#PRODUCT-----TABLE
def createTables():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
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
    conn.commit()
    conn.close()


#CREATE----PRODUCT
def createProduct(name, price, category, stock, isActive):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO Products (name, price, category, stock, isActive)
        VALUES (?, ?, ?, ?, ?);
    """, (name, price, category,stock,isActive))
    
    conn.commit()
    conn.close()
    return True

#UPDATE----PRODUCT(stock--&--status)
def updateStockStatus(id, stock, isActive):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Products SET stock = ?, isActive = ? WHERE product_id = ?", (stock, isActive, id))
    conn.commit()
    conn.close()
    return True


    #UPDATE---PRODUCT---PRICE
def updateProductPrice(id, price):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Products SET price = ? WHERE product_id = ?", (price, id))
    conn.commit()
    conn.close()
    return True
