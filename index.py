import win32gui
import time
from datetime import datetime
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
        if oldWindowName == currentWindowName:
            pass
        else:
            elapsed = time.perf_counter() - x
            windowinfo=[{'Full Detail':oldWindow},
            {'Program Name':oldWindowName},
            {'Time Elapsed':f'{round((elapsed/60),2)} min'},
            {'Time Captured':dateToday}
            ]
            # windowHist.append(windowinfo)
            x = time.perf_counter()
        # if historyAmmount < len(windowHist):
            print(windowinfo)
            # Write record to json file and



if __name__ == '__main__':
    main()

    # this is a ?