import sys
sys.path.append('./func')

import math
import ephem
import datetime
import tide_func
from moon_calc import *
import numpy as np

DIR   = './td/'
#FILE = '00OSE.TD2'

class DataRead(object):
    def __init__(self, filename):

        file_td2=DIR+filename

        #分潮の略号と番号

        TideName  = ['Sa','Ssa','Mm','MSf','Mf','2Q1','Sig1','Q1','Rho1','O1','MP1','M1', \
                     'Chi1','Pi1','P1','S1','K1','Psi1','Phi1','The1','J1','SO1','OO1','OQ2', \
                     'MNS2','2N2','Mu2','N2','Nu2','OP2','M2','MKS2','Lam2','L2',\
                     'T2','S2','R2','K2','MSN2','KJ2','2SM2','MO3','M3','SO3',\
                     'MK3','SK3', 'MN4','M4','SN4','MS4','MK4','S4','SK4','2MN6',\
                     'M6','MSN6','2MS6','2MK6','2SM6','MSK6']

        line_num = 0

        self.pl = np.zeros(60,np.float64)
        self.hr = np.zeros(60,np.float64)

        try:
            fp = open(file_td2,'r')

        except IOError as e:
            print('Cannot open %s ERR:' % file_td2,e.errno)

        else:
            for line in fp:
                line1=line.replace(" ","")
                line2=line1.replace("\n","")
                line3=line2.replace("\x1a","")
                lines=line3.split(",")

                if (line_num == 0):
                    self.name   = lines[0]
                    lat0   = float(lines[1])
                    lng0   = float(lines[2])
                    self.level  = lines[3]
                    line_num += 1

                    self.lat  = int(lat0) + (lat0-int(lat0))*100/60
                    self.lng  = int(lng0) + (lng0-int(lng0))*100/60

                else:
                    if (len(lines)>5):
                        for k in range (60):
                            if (TideName[k] == lines[0]):
                                key1 = k
                            if (TideName[k] == lines[3]):
                                key2 = k

                        self.hr[key1] = float(lines[1])
                        self.pl[key1] = float(lines[2])
                        self.hr[key2] = float(lines[4])
                        self.pl[key2] = float(lines[5])
                        line_num += 1
         
                    else:
                        exit

            fp.close()




class TideDay(object):
    def __init__(self, data_read, year, month, day):

         pt = tide_func.Port

         pt.hr = np.zeros(60,np.float64)
         pt.pl = np.zeros(60,np.float64)

         self.name = data_read.name

         pt.name = self.name
         pt.lat = data_read.lat
         pt.lng = data_read.lng
         pt.level = data_read.level

         pt.hr = data_read.hr
         pt.pl = data_read.pl

         moon = ephem.Moon()
         pt_eph = ephem.Observer()
         pt_eph.lon = pt.lng
         pt_eph.lat = pt.lat
         pt_eph.elevation = 0.0

         pt.date = str(year)+str('/%02d' % month) + str('/%02d' % day)
         pt_eph.date = str(pt.date+' 9:00')

         self.weekday = get_weekday(pt.date)

         today_moon = Moon(pt_eph)
         today_moon.noon(pt_eph)

         self.tname = today_moon.tname
         self.moon_age = today_moon.moonage

         today = tide_func.Tide(pt)
         tt = today.wav(pt)

         level = today.tl
         tide = today.tide
         self.hitide = today.hitide
         self.lowtide = today.lowtide
