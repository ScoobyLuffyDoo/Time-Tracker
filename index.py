import win32gui
import time
from datetime import datetime
import json
import sqlite3


DB_path ='./data/TimeTrackerDB.db' 
windowHist = []
dateToday = datetime.today().strftime('%Y-%m-%d')

def filterWindow(i_name):
    filteredName= i_name.replace('● ','') 
    # create a replace sting with blank (table data)
    #  name_of_window|replacement string
    # add the string to an array
    # Filter the string based on the name of the window 
    return filteredName
def filterProgramName(i_window):
    programData= i_window.split(' - ')
    programDataLenth = len(programData)
    name = programData[programDataLenth-1]
    return name

def createRecord(jsoninput,timeCaptured):
    try:
        values = str(jsoninput),str(timeCaptured)
        cursor.execute(f'insert into ActivityTable Values(?,?)',values)
        connection.commit()
        output={"message":'Record Created'}
    except sqlite3.IntegrityError as e:
        output={"message":str(e) }
    return 



def main():
    x = time.perf_counter()
    while True:
        historyAmmount = len(windowHist)
        w=win32gui 
        oldWindow = filterWindow(w.GetWindowText(w.GetForegroundWindow()))
        oldWindowName =filterProgramName(oldWindow) 
        time.sleep(2)    
        currentWindowFilter = filterWindow( w.GetWindowText(w.GetForegroundWindow()))
        currentWindowName = filterProgramName(currentWindowFilter)
        if oldWindow == currentWindowFilter:
           pass
        else:
            elapsed = round(((time.perf_counter() - x)/60),2)
            activityDetails={
                "Full Details":oldWindow,
                "Program Name":oldWindowName,       
                "Time Elapsed":f'{elapsed} min',
                "Time Captured":dateToday
            }
            jsonActivityData= json.dumps(activityDetails)
            createRecord(jsonActivityData,dateToday)                    
            x = time.perf_counter()
            
    



if __name__ == '__main__':
    try:
        connection = sqlite3.connect(DB_path)            
        cursor = connection.cursor()  
        main()
    except Exception as e:
        print(e)
    finally:
        print("program Terminated ")
        connection.close()  
        