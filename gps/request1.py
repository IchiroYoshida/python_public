import datetime
import requests

url = 'https://www1.kaiho.mlit.go.jp/KAN11/choryu/inet/Okinawa_Current_Map/'

today = datetime.date.today()

for d in range(21):
    date = today +datetime.timedelta(days=d)
    date_list = date.strftime('%Y/%m/%d').split('/')
    date_str = date_list[0]+date_list[1]+date_list[2]
    for t in range(24):
        t_str = '{:02d}'.format(t)
        fname =url+'Okinawa7_'+date_str+t_str+'.gif'
        response = requests.get(fname)
        image = response.content

        wfname = './gif/'+date_str+t_str+'.gif'

        with open(wfname, "wb") as f:
            f.write(image)
 
