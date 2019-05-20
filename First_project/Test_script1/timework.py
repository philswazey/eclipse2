'''
Created on May 8, 2019

@author: phil
'''
import os
import fnmatch
#import datetime
from datetime import date
from datetime import time
from datetime import datetime

today=datetime.now()
print (today)
    # Get the current time
    #t = datetime.time(datetime.now())
    #print "The current time is", t
    #weekday returns 0 (monday) through 6 (sunday)
wd = date.weekday(today)
    #Days start at 0 for monday
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("Today is day number %d" % wd)
print("which is a " + days[wd])