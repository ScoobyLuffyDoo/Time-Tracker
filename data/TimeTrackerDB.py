import sqlite3 
connection = sqlite3.connect("TimeTrackerDB.db")
cursor = connection.cursor()
ActivityTable_CMD = """CREATE TABLE IF NOT EXISTS
ActivityTable(
    ProgramName TEXT,
    StartTime TEXT,
    EndTime TEXT,
    TimeElapsed TEXT, 
    DateCaptured TEXT,
    FullProgramDetails TEXT
)
"""
cursor.execute(ActivityTable_CMD)
connection.close()