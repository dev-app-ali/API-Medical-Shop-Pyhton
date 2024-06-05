import sqlite3

#UPDATE---USER--LEVEL
def updateUserLevel(id,level):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE User SET level = ? WHERE id = ?", (level, id))
    conn.commit()
    conn.close()
    return True