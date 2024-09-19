import simplekml
githuburl = "https://raw.githubusercontent.com/IchiroYoshida/python_public/master/uriyasa/png/"
pngfile = "20240901N2.png"
Name = 'Kamishima'

kml = simplekml.Kml()

str1 = '<table><tr><td><img src=\"'
str2 = 'width=\"640\" height=\"480\" align=\"left\"/></td></tr><tr><td>'
str3 = '<center>'+Name+'</center></table></td></tr></table>' 
desstr = str1+githuburl+pngfile+'\" '+str2+str3
#print(desstr)

test_point = kml.newpoint(name=Name, \
      description = desstr, \
      coords=[(123.819, 24.330)]) 
  
kml.save('kamishima.kml')
