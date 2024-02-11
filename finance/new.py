"""""""""""""""""""""""
finance 2022-04-28
"""""""""""""""""""""""
import pandas as pd
import datetime

def number_converter(x):
    if ("K" in x):
        x = x.replace("K","")
        x = float(x)*1000
    elif("M" in x):
        x = x.replace("M","")
        x = float(x)*1000000
    elif("," in x):
        x = x.replace(",","")
        x = float(x)
    elif("%" in x):
        x = x.replace("%","")
        x = float(x)

    return x
 
filecsv='./data/1545/10.csv'

df = pd.read_csv(filecsv)

# 日付けをdatetimeに変換
df["日付け"] = df["日付け"].apply(lambda x: datetime.datetime.strptime(x, "%Y年%m月%d日"))


# 数値データを　floatに変換
for col in ["終値", "始値", "高値", "安値", "出来高", "変化率 %"]:
    df[col] = df[col].apply(number_converter)

print(df.head())

