from mimetypes import read_mime_types
import win32gui
import time
from datetime import datetime
import json
import sqlite3


DB_path ='./data/TimeTrackerDB.db' 
dateToday = datetime.today().strftime('%Y-%m-%d')
timeFormat = '%H:%M:%S'

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
        keys =["ProgramName","StartTime","EndTime","TotalTimeElapsed","TimeElapsed","DateCaptured","FullProgramDetails"]
        values = list(map(ProgramData.get,keys))
        cursor.execute(f'insert into ActivityTable Values(?,?,?,?,?,?,?)',values)
        connection.commit()
    except sqlite3.IntegrityError as e:
        output={"message":str(e) }
    return 
    
def formatElapsedTime(iTime):
    timeList = str(iTime).split(":")
    totalseconds = ((int(timeList[0]) *120)+(int(timeList[1]) *60)+(int(timeList[2])))
    totalMin = round((totalseconds/60),2)
    return totalMin


def main():
    # startTime =datetime.now().strftime('%H:%M:%S')
    startTime = time.strftime(timeFormat, time.localtime())
    while True:
        w=win32gui 
        oldWindow = filterWindow(w.GetWindowText(w.GetForegroundWindow()))
        oldWindowName =filterProgramName(oldWindow) 
        time.sleep(2)    
        currentWindowFilter = filterWindow( w.GetWindowText(w.GetForegroundWindow()))
        # currentWindowName = filterProgramName(currentWindowFilter)
        if oldWindow == currentWindowFilter:
           pass
        # Check if windows is in sleep mode to pause
        else:
            endTime = time.strftime(timeFormat, time.localtime())
            # convert time elapsed into readable format HH:MM::SS
            TotaltimeElapsed = datetime.strptime(endTime, timeFormat) - datetime.strptime(startTime, timeFormat)
            timeElapsed =formatElapsedTime(TotaltimeElapsed)         
            activityDetails={
                "ProgramName": oldWindowName,
                "StartTime":startTime,
                "EndTime": endTime,
                "TotalTimeElapsed": str(TotaltimeElapsed), 
                "TimeElapsed":str(timeElapsed),
                "DateCaptured": dateToday,
                "FullProgramDetails":oldWindow
            }
            createRecord(activityDetails)                    
            startTime = time.strftime(timeFormat, time.localtime())   
    return 

if __name__ == '__main__':
    # try:
    #     connection = sqlite3.connect(DB_path)            
    #     cursor = connection.cursor()  
    #     main()
    # except Exception as e:
    #     print(e)
    # finally:
    #     print("program Terminated ")
    #     connection.close()  
    connection = sqlite3.connect(DB_path)            
    cursor = connection.cursor()  
    main()
    print("program Terminated ")
    connection.close()  