lon1 = 124.301      # Start Toukei keido
lat1 =  24.488      # Start  hokui
lon2 = 124.293
lat2 =  24.476

Trace = '425'
Description  = 'MA:0.7-1 2008/08/02 Ser.425'
Ent = '10:01'
Ext = '11:02'

kmlHead = (
   '<?xml version="1.0" encoding="UTF-8"?>\n'
   '<kml xmlns="http://earth.google.com/kml/2.2">\n'
   '<Document>\n'
   )

kmlTrace = (
   '<Placemark>\n'
   '<name>Trace {:s}</name>\n'
   '<description>{:s}</description>\n'
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
   ).format(Trace, Description, lon1, lat1, lon2, lat2)

kmlEntry = (
   '<Placemark>\n'
   '<name>Entry {:s}</name>\n'
   '<Point>\n'
   '<coordinates>{:6.3f},{:6.3f}</coordinates>\n'
   '</Point>\n'
   '</Placemark>\n'
   ).format(Ent,lon1,lat1)

kmlExit = (
   '<Placemark>\n'
   '<name>Exit {:s}</name>\n'
   '<Point>\n'
   '<coordinates>{:6.3f},{:6.3f}</coordinates>\n'
   '</Point>\n'
   '</Placemark>\n'
   ).format(Ext, lon2, lat2)

kmlTail = (
   '</Document>\n'
   '</kml>\n'
   )

print(kmlHead, kmlTrace, kmlEntry, kmlExit, kmlTail)
