# 月の日数
def month_days(year,month):
    if (month < 0 or month > 12): return (-1)
    d = 0

    m = [31,31,28,31,30,31,30,31,31,30,31,30,31] # /* 各月の日数 */

    if ((year % 4 == 0 and year % 100 !=0) or year % 400 == 0 ): # 閏年
         m[2] = 29
    
    return (m[month])

"""
曜日
"""
def get_weekday(date):
    import datetime
    weekday=['月','火','水','木','金','土','日']
    d = datetime.datetime.strptime(date,"%Y/%m/%d")
    return weekday[d.weekday()]

"""
当番名簿
"""
def touban_name(n):
    touban=['野崎','三原','吉田']
    return touban[n]

"""
年間当番表
2016/11/01
"""

year = 2017

num = 0

for month in range (1,13):
    days = month_days(year,month)
    print (year,month)

    for d in range(0,days):

        num += 1
        day = d+1
        jun = num % 3

        date = str(year)+str('/%02d' % month)+str('/%02d' % day)
        wday  = get_weekday(date)

        print(date,wday,touban_name(jun))

