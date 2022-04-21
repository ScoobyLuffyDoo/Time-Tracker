import win32gui
import time
from datetime import datetime

w= win32gui
while True:
    flags, hcursor, (x,y) = w.GetCursorInfo()
    print(f'{flags}::{hcursor}::{x}::{y}')
# http://timgolden.me.uk/pywin32-docs/win32gui.html