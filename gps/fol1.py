import folium
from folium.features import CustomIcon

# 登野城漁港
office_lat = 24.3322
office_lng = 124.1638

#GoogleMap Icons
pushpin = CustomIcon(icon_image='http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png', icon_size=(30,30))
exitpoint =CustomIcon(icon_image='https://maps.google.com/mapfiles/kml/pal3/icon61.png', icon_size=(30,30)) 
sailing = CustomIcon(icon_image='https://maps.google.com/mapfiles/ms/micons/sailing.png', icon_size=(30,30))
anchoring = CustomIcon(icon_image='https://maps.google.com/mapfiles/ms/micons/marina.png', icon_size=(30,30))   

fmap1 = folium.Map(
    location=[office_lat, office_lng],
    #tiles = "OpenStreetMap",
    #tiles='https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png',
    tiles='https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{z}/{x}/{y}.jpg',
    attr='国土地理院',
    zoom_start = 12, # 描画時の倍率 1〜20
    width = 1024, height = 1024 # 地図のサイズ
) 
folium.Marker([office_lat, office_lng], icon=pushpin, popup='潜人号はここにあります').add_to(fmap1)
fmap1.save('folium1.html')
