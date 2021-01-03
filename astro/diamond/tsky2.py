"""
	Tokyo skytree 
"""
from numpy import sin,cos,tan,pi
import ephem

xx,yy = [],[]
ll =[]

fp=open("tokyo_sky.js","w")

sky = ephem.Observer()
sky.lon, sky.lat = '139.8106','35.71004'

RAD=pi/180.

Earth=6378137.0   # (m)
H=634.0           # (m)

sky.date='2015/12/06 7:00' #JST 16:00 PM
sun=ephem.Sun()

lon=float(sky.lon)
lat=float(sky.lat)

def Rambda(delta_x):
	return lon+delta_x/Earth/cos(lat)

def Phai(delta_y):
	return lat+delta_y/Earth
for ti in range(8):
	sun.compute(sky)
	th=float(sun.az)
	l=H /tan(float(sun.alt))
	ll.append(l)
	xx.append(-l*sin(th))
	yy.append(-l*cos(th))
	sky.date += ephem.hour

print ("#Tokyo Sky Tree %.6f, %.6f" %(lat/RAD,lon/RAD))
print ("#Sunset %s" %(sky.next_setting(ephem.Sun())))

for ti in range(8):
	xr=Rambda(xx[ti])
	yr=Phai(yy[ti])

	print ("%.6f, %.6f" % (yr/RAD,xr/RAD))


#Output JavaScript 
def output_js_head(fp,center):
    print >>fp,"/* Google Maps Shadow of Tokyo Skytree 2015-12-6 16:00-16:15*/"
    print >>fp,"function initialize() {"
    print >>fp,"  if (GBrowserIsCompatible()) {"
    print >>fp,"    var map = new GMap2(document.getElementById(\"map_canvas\"));"
    print >>fp, "    map.setCenter(new GLatLng("+str(center[0])+","+str(center[1])+"),13);"
    print >>fp,""

def output_js_points1(fp,center,lat,lon):
    print >>fp,"    var points1 = ["
    print >>fp,"        new GLatLng("+str(center[0])+","+str(center[1])+"),"
    print >>fp,"        new GLatLng("+str(lat[0])+","+str(lon[0])+"),"
    print >>fp,"        new GLatLng("+str(lat[1])+","+str(lon[1])+"),"
    print >>fp,"        new GLatLng("+str(lat[2])+","+str(lon[2])+"),"
    print >>fp,"        new GLatLng("+str(center[0])+","+str(center[1])+")"
    print >>fp,"    ];"
    print >>fp,""

def output_js_end(fp):    
    print >>fp,"    var line1 = new GPolygon(points1);"
    print >>fp,""
    print >>fp,"    map.addOverlay(line1);"
    print >>fp,""
    print >>fp,"  }"
    print >>fp,"}"

output_js_head(fp)
output_js_points1(fp)
output_js_end(fp)

fp.close()

