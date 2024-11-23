import sqlite3

class Database:
    def __init__(self,db,cursor):
        self.db=db
        self.cursor=cursor
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS hotels ")

bridge=sqlite3.connect('data.db')
cursor=bridge.cursor()
db=Database(bridge,cursor)


bridge.commit()
bridge.close()