import sqlite3 
connection = sqlite3.connect("TimeTrackerDB.db")
cursor = connection.cursor()
ActivityTable_CMD = """CREATE TABLE IF NOT EXISTS
ActivityTable(
    ProgramName
    timeCaptured TEXT 
)
"""
cursor.execute(ActivityTable_CMD)
connection.close()