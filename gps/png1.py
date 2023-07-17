import simplekml
githuburl = "https://raw.githubusercontent.com/IchiroYoshida/python_public/master/gps/png/"
pngfile = "20040503N2.png"
Name = 'Ser.225'

kml = simplekml.Kml()

str1 = '<table><tr><td><img src=\"'
str2 = 'width=\"640\" height=\"480\" align=\"left\"/></td></tr><tr><td>'
str3 = '<center>'+Name+'</center></table></td></tr></table>' 
desstr = str1+githuburl+pngfile+'\" '+str2+str3
#print(desstr)

test_point = kml.newpoint(name=Name, \
      description = desstr, \
      coords=[(124.1640, 24.3321)]) 
  
kml.save('png1.kml')