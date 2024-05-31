import sqlite3
import json

 #GET-----ALL-----PRODUCT
def getAllProducts():
    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * From Products")
    products = cursor.fetchall()
    conn.close()
    print(products)
    productJson=[]
    for product in products:
        tempProduct={
        "product_id" : product[0],
        " name" : product[1],
        "price" : product[2],
        "stock" : product[3],
        "isActive" : product[4],
        "category" : product[5],
        
        }

        productJson.append(tempProduct)
    return json.dumps(productJson)




 #GET-----SPECIFIC-----PRODUCT
def getSpecificProduct(productId):

    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * From products WHERE product_id=?",(productId,))
    products = cursor.fetchall()
    conn.close()
    print(products)
    productJson=[]
    for product in products:
        tempProduct={
        "product_id" : product[0],
        " name" : product[1],
        "price" : product[2],
        "stock" : product[3],
        "isActive" : product[4],
        "category" : product[5],
        

        }

        productJson.append(tempProduct)
    return json.dumps(productJson)