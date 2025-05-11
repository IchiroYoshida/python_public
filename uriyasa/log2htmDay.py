'''
 *.log and *.png ---> *.html (folium)
2024/09/17
'''

import folium
import csv
import os
import numpy as np

LOG = './log/'
PNG = '../png/'
HTM = './htm/'

Tile ="https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{z}/{x}/{y}.jpg"

str1 = "<table><tr><td><img src=\""
str2 = "width=\"640\" height=\"480\" align=\"left\"/></td></tr><tr><td>"

Date=[]
# Days
log_files = os.listdir(LOG)
log_files.sort()

for logs in log_files:
   Date.append(logs.split('N')[0])
   Days=sorted(list(set(Date)))   

for Day in Days:
    for logs in log_files:
        DayLog = logs.split('N')[0]
        if (Day == DayLog):
            # center
            Lat=[]
            Lng=[]
            with open(LOG+logs, encoding='utf8', newline='') as l:
                csvreader =csv.reader(l)
                data = [row for row in csvreader][0]
                Lat.append(float(data[1]))
                Lng.append(float(data[2]))
            try:
                Lat.append(float(data[4]))
                Lng.append(float(data[5]))
            except:
                continue
            finally:
                LatAve = '{:.3f}'.format(np.average(Lat))
                LngAve = '{:.3f}'.format(np.average(Lng))
                center =[LatAve, LngAve]
    #print(Day,center)
    fmap1 = folium.Map(
        location = center,
        tiles = Tile,
        attr = "地理院地図",
        zoom_start = 12,
        width = 2048, height = 1600
    )
    for logs in log_files:
        DayLog = logs.split('N')[0]
        if (Day == DayLog):
            with open(LOG+logs, encoding='utf8', newline='') as l:
                csvreader =csv.reader(l)
                data = [row for row in csvreader][0]
                #print(Day,logs,data)     
                DayNo = logs.split('N')[1][:1]

                YY = Day[:4]  #Year
                MM = Day[4:6] #Month
                DD = Day[6:]  #Day
       
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
            finally:
                Name = Day +' No.'+DayNo
                File_png = Day +'N'+DayNo+'.png'
                str3 = '<center>'+Name+' </center></table></td></tr></table'
                desstr = str1+PNG+File_png+'\"'+str2+str3
           
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
            else: #Style = 'A' Anchor
                Entry = [EntLat, EntLng]
                folium.Marker(location=Entry,popup=desstr,icon=folium.Icon("blue")).add_to(fmap1)
                
    File_html = HTM+Day+'.html'
    fmap1.save(File_html)