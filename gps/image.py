import simplekml

kml = simplekml.Kml()

test_point = kml.newpoint(name="Uriyasa2",
  description = '''<table><tr><td><img src="./png/20040505N2.png"
 width="500" height="500" align="left"/></td></tr>
 <tr><td>Image caption</table></td></tr></table>''',
  coords=[(124.1640, 24.3321)]) 
  
kml.save("png1.kml")
