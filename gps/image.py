import simplekml
githuburl = "https://https://github.com/IchiroYoshida/python_public/blob/master/gps/png/"

kml = simplekml.Kml()

#des1 = "<table><tr>td><img src="+githuburl+"20040505N2.png" \
#       width="500" height="500" align="left"/></td></tr><tr><td>Image caption</table> \
#       </td></tr></table>"

test_point = kml.newpoint(name="test_name", \
      description = '<img src="path/latest_image.jpg" \
      width="500" height="500" align="left"/>', \
      coords=[(124.1640, 24.3321)]) 
  
kml.save("png1.kml")
