"""
moon_func.py

月の暦に関する基礎関数
"""
import ephem
import math

#RAD=180./ephem.pi
AU = 149597870.7  #1AU (Km)


"""
曜日
"""
def get_weekday(date):
    import datetime
    weekday=['月','火','水','木','金','土','日']
    d = datetime.datetime.strptime(date,"%Y/%m/%d")
    return weekday[d.weekday()]



#
def rnd36(x):
   return (x -math.floor(x / 360) * 360)

def tidename_MoonAge(moonage):
    Name=['大潮','中潮','小潮','長潮','若潮','中潮','大潮','中潮','小潮','長潮','若潮','中潮']

    x = moonage

    if   (x< 2):  return(Name[0])
    elif (x< 6):  return(Name[1])
    elif (x< 9):  return(Name[2])
    elif (x< 10):  return(Name[3])
    elif (x< 11):  return(Name[4])
    elif (x< 13):  return(Name[5])
    elif (x< 17):  return(Name[6])
    elif (x< 21):  return(Name[7])
    elif (x< 24):  return(Name[8])
    elif (x< 25):  return(Name[9])
    elif (x< 26):  return(Name[10])
    elif (x< 28):  return(Name[11])
    else        :  return(Name[0])

def tidename_MIRC(x):
    Name=['大潮','中潮','小潮','長潮','若潮','中潮','大潮','中潮','小潮','長潮','若潮','中潮']

    if   (x< 31):  return(Name[0])
    elif (x< 67):  return(Name[1])
    elif (x<103):  return(Name[2])
    elif (x<115):  return(Name[3])
    elif (x<127):  return(Name[4])
    elif (x<163):  return(Name[5])
    elif (x<211):  return(Name[6])
    elif (x<247):  return(Name[7])
    elif (x<283):  return(Name[8])
    elif (x<295):  return(Name[9])
    elif (x<307):  return(Name[10])
    elif (x<343):  return(Name[11])
    else        :  return(Name[0])

def tidename_JMA(x):
    Name=['大潮','中潮','小潮','長潮','若潮','中潮','大潮','中潮','小潮','長潮','若潮','中潮']

    if   (x< 36):  return(Name[0])
    elif (x< 72):  return(Name[1])
    elif (x<108):  return(Name[2])
    elif (x<120):  return(Name[3])
    elif (x<132):  return(Name[4])
    elif (x<168):  return(Name[5])
    elif (x<216):  return(Name[6])
    elif (x<252):  return(Name[7])
    elif (x<288):  return(Name[8])
    elif (x<300):  return(Name[9])
    elif (x<312):  return(Name[10])
    elif (x<348):  return(Name[11])
    else        :  return(Name[0])

