# -*- coding: utf-8 -*-

def PrnJavaScript(filename,lat,lon):
    with open(filename,'w') as fp:

        print('/* Google Maps PrnJavaScript */', file = fp)
        print('function initialize() {', file = fp)
        print('  if (GBrowserIsCompatible()) {', file = fp)
        print('    var map = new GMap2(document.getElementById(\"map_canvas\"));', file = fp)
        print(('    map.setCenter(new GLatLng( %f, %f),5);' % (35.6929, 140.8653)), file = fp)

        print('', file = fp)
        print('    var points1 = [', file = fp)

        n=len(lat)

        for i in range(n):
            print(('        new GLatLng( %f, %f),' % (float(lat[i]), float(lon[i]))), file = fp)

        print('    ];', file = fp)
        print('', file = fp)
        print('    var line1 = new GPolyline(points1);', file = fp)
        print('', file = fp)
        print('    map.addOverlay(line1);', file = fp)
        print('', file = fp)
        print('  }', file = fp)
        print('}', file = fp)

    fp.close()
