def PrnJavaScript(filename,lat,lon):
    with open(filename, mode='w') as fp:

        fp.write('/* Google Maps PrnJavaScript */\n')
        fp.write('function initMap() {\n')
        fp.write('   var map = new google.maps.Map(document.getElementById(\'map\'),{\n')
        fp.write('      zoom: 5,\n')
        fp.write('      center: {lat: '+str(lat[0])+', lng: '+str(lon[0])+'},\n')
        fp.write('      mapTypeID: \'terrain\' \n')
        fp.write('});\n')

        n=len(lat)

        fp.write('var triangleCoords = [\n')
        for i in range(n):
            fp.write('        {lat: '+str(lat[i])+', lng: '+str(lon[i])+'},\n')
        fp.write('        {lat: '+str(lat[0])+', lng: '+str(lon[0])+'}\n')
        fp.write('];\n')
        fp.write('\n')
        fp.write('// Construct the polygon.\n')
        fp.write(' var sunTriangle = new google.maps.Polygon({\n')
        fp.write('    paths: triangleCoords,\n')
        fp.write('    strokeColor: \'#FF0000\',\n')
        fp.write('    strokeOpacity: 0.8,\n')
        fp.write('    strokeWeight: 2,\n')
        fp.write('    fillColor: \'#FF0000\',\n')
        fp.write('    fillOpacity: 0.35\n')
        fp.write('});\n')
        fp.write('sunTriangle.setMap(map);\n')
        fp.write('}\n')
