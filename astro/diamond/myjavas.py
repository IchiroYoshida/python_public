def PrnJavaScript(filename,lat,lon):
    with open(filename, mode='w') as fp:

        fp.write('/* Google Maps PrnJavaScript */')
        fp.write('function initialize() {')
        fp.write('  if (GBrowserIsCompatible()) {')
        fp.write('    var map = new GMap2(document.getElementById(\'map_canvas\'));')
        fp.write( '    map.setCenter(new GLatLng('+str(lat[0])+','+str(lon[0])+'),13);')
        fp.write('')
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

