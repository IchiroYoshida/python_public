def PrnJavaScript(filename,lat,lon):
    with open(filename, mode='w') as fp:

        fp.write('/* Google Maps PrnJavaScript */\n')
        fp.write('function initialize() {\n')
        fp.write('   if (GBrowserIsCompatible()){\n')
        fp.write('       var map = new GMap2(document.getElementById("map_canvas"));\n')
        fp.write('       map.setCenter(new GLatLng('+str(lat[0])+', '+str(lon[0])+'),13);\n')
        fp.write('       var points1 = [\n')

        n=len(lat)

        for i in range(n):
            fp.write('        new GLatLng('+str(lat[i])+','+str(lon[i])+'),\n')

        fp.write('        new GLatLng('+str(lat[0])+','+str(lon[0])+')\n')
        fp.write('    ];\n')
        fp.write('\n')
        fp.write('    var line1 = new GPolygon(points1);\n')
        fp.write('\n')
        fp.write('    map.addOverlay(line1);\n')
        fp.write('\n')
        fp.write('  }\n')
        fp.write('}\n')

