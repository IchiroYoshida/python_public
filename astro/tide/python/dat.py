#!/usr/bin/python
import sys         # use system library
level = []

for line in sys.stdin:
   line0 = line.strip()
   if (len(line0)):
      data = line0.rsplit(' ',1)
      level.append(int((data[-1])))
    
print (level)
