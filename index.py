import win32gui
import time
from datetime import datetime
import json
import sqlite3


DB_path ='./data/TimeTrackerDB.db' 
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

def createRecord(ProgramData):
# def createRecord(jsoninput,timeCaptured):
    try:
        keys =["ProgramName","StartTime","EndTime","TimeElapsed","DateCaptured","FullProgramDetails"]
        values = list(map(ProgramData.get,keys))
        cursor.execute(f'insert into ActivityTable Values(?,?,?,?,?,?)',values)
        connection.commit()
    except sqlite3.IntegrityError as e:
        output={"message":str(e) }
    return 



def main():
    startTime =datetime.now().strftime('%H:%M:%S')
    x = time.perf_counter()
    while True:
        w=win32gui 
        oldWindow = filterWindow(w.GetWindowText(w.GetForegroundWindow()))
        oldWindowName =filterProgramName(oldWindow) 
        time.sleep(2)    
        currentWindowFilter = filterWindow( w.GetWindowText(w.GetForegroundWindow()))
        # currentWindowName = filterProgramName(currentWindowFilter)
        if oldWindow == currentWindowFilter:
           pass
        else:
            endTime = datetime.now().strftime('%H:%M:%S')
            # convert time elapsed into readable format HH:MM::SS
            elapsed = round(((time.perf_counter() - x)/60),2)
            activityDetails={
                "ProgramName": oldWindowName,
                "StartTime":startTime,
                "EndTime": endTime,
                "TimeElapsed": elapsed, 
                "DateCaptured": dateToday,
                "FullProgramDetails":oldWindow
            }
            # print(activityDetails)
            createRecord(activityDetails)                    
            x = time.perf_counter()
            startTime =datetime.now().strftime('%H:%M:%S')
     

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
        