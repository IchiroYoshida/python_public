'''
MACD AI3 2022-05-15
'''
from audioop import cross
import math
from pickle import STACK_GLOBAL
from pandas_datareader import data
import pandas as pd

Num = 0
Cash = 400 * 10000
Cash0 = Cash

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
    if(object.MACDHist > 0):
        res = 1
    else:
        res = -1
    return(res)

def OpeJudge(area, macd):
    ope = 0
    if (area == 5 and macd < 0):
        ope = -1
    elif (area == 0 and macd > 0):
        ope = 1
                
    return(ope)

df = pd.read_csv('data/DOW/DJI2017Ana.csv')
df = df.set_index('Date')
    
# calculate after starting day
df2 = df['2018-01-01':'2022-05-01']

days = df2.index.tolist()
end = len(days)

#Start

day_data =df2.iloc[0]

st = Stock(day_data)
area_flg = area(st)
macd_flg = MACD_flag(st)
Value0=st.Open

#ope=OpeJudge(area_flg, macd_flg)
ope = 1

#Loop
for day in range(1, end-1):
    day_data = df2.iloc[day]
    st = Stock(day_data)
    
    area_flg = area(st)
    macd_flg = MACD_flag(st)
   
    StVal = st.Open
    
    if (ope > 0):
        Num = 100
        Cash -= 100*StVal
    elif (ope < 0):
        Cash += 100*StVal
        Num = 0
        
    StAll = Num * StVal
    Total = Cash + StAll
    per0 = StVal/Value0
    per1 = Total/Cash0
   
    ope_str = '{:+3}'.format(ope) 
    Num_str = '{:4}'.format(Num)
    Val_str = '{:6}'.format(StVal)
    stA_str = '{:8}'.format(StAll)
    Cas_str = '{:8}'.format(Cash)
    Tot_str = '{:8}'.format(Total)
    per0_str = '{:4.2f}'.format(per0)
    per1_str = '{:4.2f}'.format(per1)
        
    print(days[day],ope_str,Num_str,Val_str,stA_str,Cas_str,Tot_str,per0_str,per1_str)

    ope=OpeJudge(area_flg,macd_flg) 
