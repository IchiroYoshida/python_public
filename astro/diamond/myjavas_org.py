def PrnJavaScript(filename,lat,lon):
    fp=open(filename,"w")

    print >>fp,"/* Google Maps PrnJavaScript */"
    print >>fp,"function initialize() {"
    print >>fp,"  if (GBrowserIsCompatible()) {"
    print >>fp,"    var map = new GMap2(document.getElementById(\"map_canvas\"));"
    print >>fp, "    map.setCenter(new GLatLng("+str(lat[0])+","+str(lon[0])+"),13);"

    print >>fp,""
    print >>fp,"    var points1 = ["

    n=len(lat)

    for i in range(n):
        print >>fp,"        new GLatLng("+str(lat[i])+","+str(lon[i])+"),"

    print >>fp,"        new GLatLng("+str(lat[0])+","+str(lon[0])+")"
    print >>fp,"    ];"
    print >>fp,""
    print >>fp,"    var line1 = new GPolygon(points1);"
    print >>fp,""
    print >>fp,"    map.addOverlay(line1);"
    print >>fp,""
    print >>fp,"  }"
    print >>fp,"}"

    fp.close()
