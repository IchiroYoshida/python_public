'''
MACD AI1 1 2022-05-14
'''
from audioop import cross
import math
from pandas_datareader import data
import pandas as pd

Num = 0

class Stock(object):
    def __init__(self, day_stock):
        self.High = math.floor(day_stock['High'])
        self.Low = math.floor(day_stock['Low'])
        self.Open = math.floor(day_stock['Open'])
        self.Close = math.floor(day_stock['Close'])
        self.Volume = day_stock['Volume']
        # Status
        self.Ma25 = day_stock['Ma25']
        self.Ma75 = day_stock['Ma75']
        self.MaSignal = day_stock['Ma Signal']
        self.MACD = day_stock['MACD']
        self.MACDSignal = day_stock['MACD Signal']
        self.MACDHist = day_stock['MACD Hist']
        self.RSI = day_stock['RSI']        

def area(object):
    if (object.MaSignal >1): # Ma25 > Ma75 Golden cross
        if (object.Close > object.Ma25): #A
            res = 5
        elif(object.Close < object.Ma75):#C
            res = 3
        else: #B
            res = 4
    else:
        if (object.Close > object.Ma75): #D
            res = 2
        elif(object.Close < object.Ma25):#F
            res = 0
        else: #E
            res = 1
    return(res)

def MACD_flag(object):
    if(object.MACDHist >0):
        res = 1
    elif(object.MACDHist <0):
        res = -1
    else:
        res = 0
    return(res)

def OpeJudge(area, macd):
    ope = 0
                
    return(ope)

df = pd.read_csv('data/DOW/DJI2017Ana.csv')
df = df.set_index('Date')

    
# calculate after starting day
df2 = df['2018-01-01':'2022-05-01']

days = df2.index.tolist()
end = len(days)

#Start
num = 0
SumHist = 0

day_data =df2.iloc[0]

st = Stock(day_data)
area_flg = area(st)
macd_flg = MACD_flag(st)
print(days[0],area_flg,macd_flg)

macd_flg_old = macd_flg
SumHIST = 0

#Loop
for day in range(1,end-1):
    day_data = df2.iloc[day]
    st = Stock(day_data)
    area_flg = area(st)
    macd_flg = MACD_flag(st)
   
    Val = st.Open
    MACD = st.MACD
    HIST = st.MACDHist
    SumHIST  += HIST
    
    if(macd_flg_old <0 and macd_flg>0): #Buy
        print('Buy ',Val, MACD,SumHIST)
        SumHIST = 0
    elif(macd_flg_old >0 and macd_flg <0):#Sell
        print('Sell',Val, MACD,SumHIST)
        SumHIST =0
            
    area_str = '{:2}'.format(area_flg)
    macd_str = '{:+8.1f}'.format(st.MACD)
    hist_str = '{:+8.1f}'.format(st.MACDHist)
    val_str = '{:6}'.format(st.Open)
    #ope_str  = '{:+2}'.format(ope)
    #num_str = '{:3}'.format(Num)
    
    print(days[day],area_str,val_str,macd_str,hist_str)
    macd_flg_old = macd_flg
    