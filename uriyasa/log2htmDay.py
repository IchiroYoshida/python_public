'''
 *.log and *.png ---> *.html (folium)
2024/09/17
'''

import folium
import csv
import os
import numpy as np

LOG = './LOG/2024log/'
PNG = './PNG/2024png/'
#HTM = './HTM/2024htm/'
HTM = ''

Tile ="https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{z}/{x}/{y}.jpg"

githuburl = "https://github.com/IchiroYoshida/python_public/blob/master/uriyasa/PNG/2024png/"
#githuburl = ''
str1 = "<table><tr><td><img src=\""
str2 = "width=\"640\" height=\"480\" align=\"left\"/></td></tr><tr><td>"

# center
log_files = os.listdir(LOG)
log_files.sort()

Lat=[]
Lng=[]

for date in log_files:  #[:3]:
    with open(LOG+date, encoding='utf8', newline='') as l:
        csvreader =csv.reader(l)
        data = [row for row in csvreader][0]
        
        Lat.append(float(data[1]))
        Lng.append(float(data[2]))
        
        try:
            Lat.append(float(data[4]))
            Lng.append(float(data[5]))
        except:
            continue
LatAve = '{:.3f}'.format(np.average(Lat))
LngAve = '{:.3f}'.format(np.average(Lng))
center =[LatAve, LngAve]

fmap1 = folium.Map(
    location = center,
    tiles = Tile,
    attr = "地理院地図",
    zoom_start = 12,
    width = 2048, height = 1600
)

for date in log_files:  #[:3]:
    with open(LOG+date, encoding='utf8', newline='') as l:
        csvreader =csv.reader(l)
        data = [row for row in csvreader][0]
        
        Date = date.replace('.log','').split('N')
        date = Date[0]
        DayNo = Date[1]

        YY = date[:4]  #Year
        MM = date[4:6] #Month
        DD = date[6:]  #Day
       
        EntT   = data[0]  #Entry
        EntLat = float(data[1])
        EntLng = float(data[2])
        
        ExtT   = data[3]  #Exit
        try:
            ExtLat = float(data[4])
            ExtLng = float(data[5])
            Style = 'D'
        except:
            Style = 'A'

        Name = date+' No.'+DayNo
        File_png = date+'N'+DayNo+'.png'
        str3 = '<center>'+Name+' </center></table></td></tr></table'
        desstr = str1+githuburl+File_png+'\"'+str2+str3
           
        if(Style == 'D'):   
            MidLat = (EntLat+ExtLat)/2.
            MidLng = (EntLng+ExtLng)/2.
            Entry = [EntLat, EntLng]
            Exit  = [ExtLat, ExtLng]
            Mid   = [MidLat, MidLng]

            #Entry point
            folium.Marker(location=Entry,popup=desstr,icon=folium.Icon("orange")).add_to(fmap1)
                
            if (EntLat < ExtLat) : #Go North!
                folium.PolyLine([Entry, Exit], color='#FF00FF', weight=3).add_to(fmap1)
            else: # Go South!
                folium.PolyLine([Entry, Exit], color='#00FFFF', weight=3).add_to(fmap1)

File_html = HTM+date+'.html'
fmap1.save(File_html)