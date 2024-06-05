import sqlite3
import json

 #GET-------ALL-----USER
def getAllUsers():
    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * From User")
    users = cursor.fetchall()
    conn.close()
    print(users)
    userJson=[]
    for user in users:
        tempUser={
        "id" : user[0],
        "user_id" : user[1],
        "password" : user[2],
        "level" : user[3],
        "dateOfAccountCreation" : user[4],
        "approved" : user[5],
        "blocked" : user[6],
        "name" : user[7],
        "address" : user[8],
        "email" : user[9],
        "phone" : user[10],
        "pinCode" : user[11],

        }

        userJson.append(tempUser)
    return json.dumps(userJson)



 #GET-----SPECIFIC-----USER
def getSpecificUser(userId):

    conn=sqlite3.connect("my_medicalShop.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * From User WHERE user_id=?",(userId,))
    users = cursor.fetchall()
    conn.close()
    print(users)
    userJson=[]
    for user in users:
        tempUser={
        "id" : user[0],
        "user_id" : user[1],
        "password" : user[2],
        "level" : user[3],
        "dateOfAccountCreation" : user[4],
        "approved" : user[5],
        "blocked" : user[6],
        "name" : user[7],
        "address" : user[8],
        "email" : user[9],
        "phone" : user[10],
        "pinCode" : user[11],

        }

        userJson.append(tempUser)
    return json.dumps(userJson)
