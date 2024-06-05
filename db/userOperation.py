import sqlite3

#APPROVE

def isApproved(id, approved):
  conn = sqlite3.connect("my_medicalShop.db")
  cursor = conn.cursor()

  cursor.execute("""
      UPDATE User SET approved = ? WHERE id = ?
  """, (approved,  id))

  conn.commit()
  conn.close()
  return True


#BLOCK

def isBlocked(id, blocked):
  conn = sqlite3.connect("my_medicalShop.db")
  cursor = conn.cursor()

  cursor.execute("""
      UPDATE User SET blocked = ? WHERE id = ?
  """, (blocked,  id))

  conn.commit()
  conn.close()
  return True
    



