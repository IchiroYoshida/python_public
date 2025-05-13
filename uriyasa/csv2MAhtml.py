'''
./csv/AllLogs.csv and *.png ---> MoonAge*.html (folium)
2025/05/13
'''
import folium
import csv
import os

CSV = './csv/AllLogs.csv'
PNG = './png/'
HTML = './html/'

Tile ="https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{z}/{x}/{y}.jpg"

githuburl = 'https://raw.githubusercontent.com/IchiroYoshida/python_public/master/uriyasa/png/'
str1 = '<table><tr><td><img src=\"'
str2 = 'width=\"640\" height=\"480\" align=\"left\"/></td></tr><tr><td>'

Title ="Diving Logs of Uriyasa 2003 - 2025."

center = [24.301, 123.986]

with open(CSV, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    data = [row for row in csvreader]
    del data[:1]  #Remove CSV header

for MA in range(30):
    MoonAgeName = 'MoonAge'+str(MA)

    fmap1 = folium.Map(
        location = center,
        tiles = Tile,
        attr = "地理院地図",
        zoom_start = 12,
        width = 2048, height = 1600
    )

    for dat in data:
        print(dat)
        MoonAge = float(dat[2]) #MoonAge
        if (MA <= MoonAge < (MA+1)):
            Date   = dat[1] #Date
            DayNo  = dat[3] #Tanks of the day
            EntT   = dat[4] #Entry Time
            EntLat = float(dat[5]) #Entry Latitude
            EntLng = float(dat[6]) #Entry Longitude
            ExtT   = dat[7] #Exit Time
            try:
                ExtLat =float(dat[8]) #Exit Latitude
                ExtLng = float(dat[9]) #Exit Longitude
                Style = 'D'
            except:
                Style = 'A'
            date0 = Date.replace('/','')
            Name = Date+' No.'+DayNo
            NamePNG = date0+'N'+DayNo+'.png'
            str3 = '</table></td>/</tr></table'
            desstr = str1+githuburl+NamePNG+'\"'+str2+str3

            if(Style == 'D'):   
                Entry = [EntLat, EntLng]
                Exit  = [ExtLat, ExtLng]
                print(Name,Entry,Exit)

                #Entry point
                folium.Marker(location=Entry,popup=desstr,icon=folium.Icon("orange")).add_to(fmap1)
                
                if (EntLat < ExtLat) : #Go North!
                    folium.PolyLine([Entry, Exit], color='#FF00FF', weight=3).add_to(fmap1)
                else: # Go South!
                    folium.PolyLine([Entry, Exit], color='#00FFFF', weight=3).add_to(fmap1)

            elif(Style == 'A'):
                Entry = [EntLat, EntLng]
                print(Name,Entry)

                #Entry point
                folium.Marker(location=Entry,popup=desstr,icon=folium.Icon("orange")).add_to(fmap1)
    
    fmap1.get_root().html.add_child(folium.Element(Title))
    File_html = HTML+MoonAgeName+'.html'
    print(File_html)
    fmap1.save(File_html)