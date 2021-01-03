longitude = 124.000      # keido
latitude  =  24.123      # hokui


kml = (
   '<?xml version="1.0" encoding="UTF-8"?>\n'
   '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
   '<Placemark>\n'
   '<name>Test Placemark</name>\n'
   '<Point>\n'
   '<coordinates>{:6.3f}, {:6.3f}</coordinates>\n'
   '</Point>\n'
   '</Placemark>\n'
   '</kml>'
   ).format(longitude, latitude)
print('Content-Type: application/vnd.google-earth.kml+xml\n')
print(kml)
