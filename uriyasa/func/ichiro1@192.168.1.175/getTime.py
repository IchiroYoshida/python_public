import time, datetime

def now_milliseconds():
   return int(time.time() * 1000)

# reference time.time
# Return the current time in seconds since the Epoch.
# Fractions of a second may be present if the system clock provides them.
# Note: if your system clock provides fractions of a second you can end up 
# with results like: 1405821684785.2 
# our conversion to an int prevents this

def date_time_milliseconds(date_time_obj):
   return int(time.mktime(date_time_obj.timetuple()) * 1000)

# reference: time.mktime() will
# Convert a time tuple in local time to seconds since the Epoch.

mstimeone = now_milliseconds()

mstimetwo = date_time_milliseconds(datetime.datetime.utcnow())

# value of mstimeone
# 1405821684785
# value of mstimetwo
# 1405839684000

print(mstimeone, mstimetwo)

