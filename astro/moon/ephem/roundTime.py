import datetime

def roundTime(dt=None, roundTo=60):
    if dt == None : dt = datetime.datetime.now()
    seconds = (dt- dt.min).seconds

    rounding = (seconds+roundTo/2) // roundTo * roundTo
    return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)

"""
print (roundTime(datetime.datetime(2012,12,31,23,44,59,1234),roundTo=60*60))
print (roundTime(datetime.datetime(2012,12,31,23,44,59,1234),roundTo=30*60))
print (roundTime(datetime.datetime(2012,12,31,23,56,31,1234),roundTo=1*60))
print (roundTime(datetime.datetime(2012,12,31,23,59,31,1234),roundTo=1*60))
"""

