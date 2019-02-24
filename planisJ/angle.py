import ephem
date = '2018/9/22 12:00:00'
venus = ephem.Venus()
mars = ephem.Mars()
venus.compute(date)
mars.compute(date)
sep = ephem.separation(venus,mars)
print(sep)

