
from datetime import datetime
import time
import sys

now = datetime.now()

hrs = now.hour
min = now.minute
sec = now.second

while hrs<24: #23 hours
    while min<60: #59 min
        while sec<60: #59 sec
            current = str(hrs).zfill(2) + " : " + str(min).zfill(2) + " : " + str(sec).zfill(2) + "\r"
            sys.stdout.write(current)
            sec += 1
            time.sleep(1)
        min += 1
        sec = 0
    hrs += 1
    min = 0