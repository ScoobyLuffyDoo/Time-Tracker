import sqlite3 
connection = sqlite3.connect("TimeTrackerDB.db")
cursor = connection.cursor()
clear_DB = "DELETE FROM ActivityTable where TimeCaptured = '2022-04-21'; "
cursor.execute(clear_DB)
connection.commit()
connection.close()