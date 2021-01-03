"""
# 2-4 Calender  

# LIST 2-1 MJD,JULIAN
# LIST 2-2 JDATE
 
"""
from mjd import ModifiedJulianDay
from date import MjdToDate

week=["SUN","MON","TUE","WED","THI","FRI","SAT"]

mjd=ModifiedJulianDay(2014,5,10)

wk=(mjd-4) % 7
 
print week[wk]


