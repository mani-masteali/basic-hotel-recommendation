import sqlite3

class Database:
    def __init__(self,db,cursor):
        self.db=db
        self.cursor=cursor
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS hotels (name text PRIMARY KEY, location text, star real, rate real, location_rate real, price real, sustainable bool, centre_distance real)")
        self.db.commit()
        self.db.close()

bridge=sqlite3.connect('data.db')
cursor=bridge.cursor()
db=Database(bridge,cursor)
db.create_table()