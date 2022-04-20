import win32gui
import time
windowHist = []


def filterWindow(i_name):
    filteredName= i_name.replace('● ','') 
    # create a replace sting with blank (table data)
    #  name_of_window|replacement string
    # add the string to an array
    # Filter the string based on the name of the window 
    return filteredName

def main():
    x = time.perf_counter()
    while True:
        historyAmmount = len(windowHist)
        w=win32gui 
        oldWindow = filterWindow(w.GetWindowText(w.GetForegroundWindow()))
        time.sleep(2)    
        currentWindow = filterWindow( w.GetWindowText(w.GetForegroundWindow()))
        if oldWindow == currentWindow:
            pass
        else:
            elapsed = time.perf_counter() - x
            windowHist.append([{'Name':oldWindow},{'Time Elapsed':elapsed},{'Time Captured': datetime.now()}])
            # windowHist.append({{oldWindow:round((elapsed/60),3)})
            x = time.perf_counter()
        if historyAmmount < len(windowHist):
            print(windowHist)



if __name__ == '__main__':
    main()

    # this is a ?