# 年次毎の60分潮データ取得と保存
# 2019-06-22 Ichiro Yoshida

year = '2019'

import urllib.request
from html.parser import HTMLParser

# 気象庁　潮位掲載地点一覧表の読み込み
url0 = 'http://www.data.jma.go.jp/kaiyou/db/tide/suisan/station.php'
url1 = 'http://www.data.jma.go.jp/kaiyou/db/tide/suisan/harms60.php?stn='
url2 = '&year='+year+'&tyear='+year

CompSymb  = ['Sa','Ssa','Mm','MSf','Mf','2Q1','Sig1','Q1','Rho1','O1','MP1','M1', \
             'Chi1','Pi1','P1','S1','K1','Psi1','Phi1','The1','J1','SO1','OO1','OQ2', \
             'MNS2','2N2','Mu2','N2','Nu2','OP2','M2','MKS2','Lam2','L2',\
             'T2','S2','R2','K2','MSN2','KJ2','2SM2','MO3','M3','SO3',\
             'MK3','SK3', 'MN4','M4','SN4','MS4','MK4','S4','SK4','2MN6',\
             'M6','MSN6','2MS6','2MK6','2SM6','MSK6']


def lonlatdeg(list):
    degs = []
    for i in list:
       dst = i.translate(str.maketrans('\'',' ')).split('゜')
       nn = int(dst[0])+float(dst[1])/60.
       degs.append("%.2f" % nn)
    return(degs)

class JMAParser1(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.mtx = False
        self.td = False
        self.data = []
        self.list = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "tr" and "class" in attrs:
            if "mtx" == attrs["class"]:
                self.mtx = True

        if tag == "td":
            self.td = True

        if tag == "td" and "colspan" in attrs:
            self.td = False

    def handle_endtag(self, tag):
        if tag == "td":
            self.td = False

        if tag == "tr":
            self.mtx = False

    def handle_data(self, data):
        if self.mtx and self.td:
            self.list.append(data)

class JMAParser2(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data2 = False
        self.left = False
        self.th = False
        self.thcount = 0
        self.td = False
        self.sub = False
        self.data = []
        self.list = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table" and "class" in attrs and attrs['class'] == "data2":
            self.data2 = True

        if tag == "th" and "align" in attrs and attrs['align'] == "left":
            self.left = True
            self.thcount += 1 
        if tag == "th":
            self.thcount += 1
            self.th = True

        if tag == "sub":
            self.sub = True

    def handle_endtag(self, tag):
        if tag == "th":
            self.th = False

        if tag == "tr":
            self.tr = False
            self.left = False
            self.td = False
            self.th = False
            self.thcount = 0

        if tag == "sub":
            self.sub = False

    def handle_data(self, data):
        if self.data2 and self.left:
            if self.thcount == 3:
                self.list.append(data)


with urllib.request.urlopen(url0) as response:
    html = response.read()
    html_utf8 = html.decode('utf-8')
    response.close()

parser = JMAParser1()
parser.feed(html_utf8)

No = parser.list[0::18]        # 番号
Symbol = parser.list[1::18]    # 地点番号
Name = parser.list[2::18]      # 掲載地点名
Lat = lonlatdeg(parser.list[3::18]) # 緯度（北緯）
Lon = lonlatdeg(parser.list[4::18]) # 経度（東経）
MSL1 = parser.list[5::18]      # MSL-潮位表基準面(cm)
MSL2 = parser.list[6::18]      # MSLの標高(cm)
Alt = parser.list[7::18]       # 潮位表基準面の標高(cm)
M2cm = parser.list[8::18]      # M2 振幅(cm)
M2deg = parser.list[9::18]     # M2 遅角(deg)
S2cm = parser.list[10::18]     # S2 振幅(cm)
S2deg = parser.list[11::18]    # S2 遅角(deg)
K1cm = parser.list[12::18]     # K1 振幅(cm)
K1deg = parser.list[13::18]    # K1 遅角(deg)
O1cm = parser.list[14::18]     # O1 振幅(cm)
O1deg = parser.list[15::18]    # O1 遅角(deg)
Year = [y.split('年')[0] for y in parser.list[16::18]]  # 分潮一覧表（年）
Note = parser.list[17::18]     # 備考


for no in No:
    n = int(no) - 1
    if year in Year[n]:
        url = url1 + Symbol[n] + url2

        with urllib.request.urlopen(url) as response:
            html_utf8 = response.read().decode('utf-8')
            response.close()
    
        parser = JMAParser2()
        parser.feed(html_utf8)

        Speed = parser.list[0::3]
        Amp = parser.list[1::3]
        Deg = parser.list[2::3]

        file_name = './'+year+'/' + Name[n] + '.TD3'
        f = open(file_name,'w')

        str = '{0:<},'.format(Name[n])+\
              '{:>6},'.format(Lat[n])+\
              '{:>6},'.format(Lon[n])+\
              '{:>5}'.format(MSL1[n])+'\n'
        f.write(str)

        for n in range(0,60, 2):
            str = '{:<4},'.format(CompSymb[n])+\
                  '{:>5},'.format(Amp[n])+\
                  '{:>6},'.format(Deg[n])+\
                  '      '+\
                  '{:<4},'.format(CompSymb[n+1])+\
                  '{:>5},'.format(Amp[n+1])+\
                  '{:>6}'.format(Deg[n+1])+'\n'
            f.write(str)
        f.close()
