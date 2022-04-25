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
sql = "SELECT ProgramName,TotalTimeElapsed,DateCaptured FROM ActivityTable"
cursor.execute(sql)
output = cursor.fetchall()   
connection.close()        


columnNames =["ProgramName","TotalTimeElapsed", "DateCaptured"]
df =pd.DataFrame(output,columns=columnNames)
df2 = df.groupby('ProgramName')['TimeElapsed'].sum()

print(df)
# for row in  output:
#     print(row)        


# data = {"pogramName":[],"timeElapsed":[],"capture Date":[]}

# sns.relplot(x="timepoint", y="signal", hue="region", style="event",
#             kind="line", data=fmri);
# plt.show()