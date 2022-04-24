import sqlite3 
connection = sqlite3.connect("TimeTrackerDB.db")
cursor = connection.cursor()
clear_DB = "DELETE FROM ActivityTable; "
cursor.execute(clear_DB)
connection.commit()
connection.close()