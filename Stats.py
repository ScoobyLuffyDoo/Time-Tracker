import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
sns.set_theme(style="darkgrid")

DB_path ='./data/TimeTrackerDB.db'

try:
    connection = sqlite3.connect(DB_path)
    # connection.row_factory = sqlite3.Row 
except Exception as e:
    print(e)
cursor = connection.cursor()
sql = "SELECT ProgramName,TimeElapsed,DateCaptured FROM ActivityTable"
cursor.execute(sql)
output = cursor.fetchall()   
connection.close()        


columnNames =["ProgramName","TimeElapsed", "DateCaptured"]
df =pd.DataFrame(output,columns=columnNames)
print(df)
df2 = df.groupby(['ProgramName' , 'DateCaptured']).sum()


sns.relplot(x="DateCaptured", y="TimeElapsed", style="ProgramName",
            kind="line", data=df);
plt.show()