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
sql = "SELECT ProgramName,TimeElapsed,DateCaptured FROM ActivityTable Where ProgramName = 'Visual Studio Code' or ProgramName ='Opera'"
cursor.execute(sql)
output = cursor.fetchall()   
connection.close()        


columnNames =["ProgramName","TimeElapsed", "TimeCaptured"]
df =pd.DataFrame(output,columns=columnNames)
print(df)
df2 = df.groupby(['ProgramName' , 'TimeCaptured']).sum()


sns.lineplot(x="TimeCaptured", y="TimeElapsed", hue="ProgramName",
            data=df);
plt.show()