lon1 = 124.301      # Start Toukei keido
lat1 =  24.488      # Start  hokui
lon2 = 124.293
lat2 =  24.476
doc  = '2008/08/02-2 MA=0.7 Ser.425'

kml = (
   '<?xml version="1.0" encoding="UTF-8"?>\n'
   '<kml xmlns="http://earth.google.com/kml/2.2">\n'
   '<Document>\n'
   '<Placemark>\n'
   '<name>Trace 123</name>\n'
   '<description>{:s}</description>'
   '<LineString>\n'
   '<coordinates>{:6.3f},{:6.3f} {:6.3f},{:6.3f}</coordinates>\n'
   '</LineString>\n'
   '<Style>\n'
   '<LineStyle>\n'
   '<color>ffff0000</color>\n'
   '<width>4</width>\n'
   '</LineStyle>\n'
   '</Style>\n'
   '</Placemark>\n'
   '<Placemark>\n'
   '<name>Entry 10:00</name>\n'
   '<Point>\n'
   '<coordinates>{:6.3f}, {:6.3f}</coordinates>\n'
   '</Point>\n'
   '</Placemark>\n'
   '<Placemark>\n'
   '<name>Exit 11:00</name>\n'
   '<Point>\n'
   '<coordinates>{:6.3f}, {:6.3f}</coordinates>\n'
   '</Point>\n'
   '</Placemark>\n'
   '</Document>\n'
   '</kml>\n'
   ).format(doc,lon1,lat1,lon2,lat2,lon1,lat1,lon2,lat2)
print(kml)
