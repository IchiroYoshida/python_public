import ephem
import math

location = ephem.Observer()

location.name = 'Fukuoka'
location.lon, location.lat = '130.391', '33.593'
location.date = '2018/06/25 12:00:00' #21:00 JST

p = ephem.FixedBody(ra=0.0, dec=0.0)

p.compute(location)

print(p.alt,p.az)
