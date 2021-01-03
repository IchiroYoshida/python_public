def PrnJavaScript(filename,lat,lon):
    with open(filename, mode='w') as fp:

        fp.write('/* Google Maps PrnJavaScript */\n')
        fp.write('function initialize() {\n')
        fp.write('   var latlng = new google.maps.LatLng('+str(lat[0]+','+str(lon[0]+');\n'
        fp.write('    var points1 = [')

        n=len(lat)

        for i in range(n):
            fp.write('        new GLatLng('+str(lat[i])+','+str(lon[i])+'),')

        fp.write('        new GLatLng('+str(lat[0])+','+str(lon[0])+')')
        fp.write('    ];')
        fp.write('')
        fp.write('    var line1 = new GPolygon(points1);')
        fp.write('')
        fp.write('    map.addOverlay(line1);')
        fp.write('')
        fp.write('  }')
        fp.write('}')

