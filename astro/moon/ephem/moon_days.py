# 月の日数
def month_days(year,month):
    if (month < 0 or month > 12): return (-1)
    d = 0

    m = [31,31,28,31,30,31,30,31,31,30,31,30,31] # /* 各月の日数 */

    if ((year % 4 == 0 and year % 100 !=0) or year % 400 == 0 ): # 閏年
         m[2] = 29
    
    return (m[month])


# 年初からの経過日数 
def day_serial(year,month,day):
    d = 0
    m = [31,31,28,31,30,31,30,31,31,30,31,30,31] # /* 各月の日数 */

    if ((year % 4 == 0 and year % 100 !=0) or year % 400 == 0 ): # 閏年
         m[2] = 29
    
    for  i in range (1,month):
         d += m[i]
    d += day - 1

    return d


