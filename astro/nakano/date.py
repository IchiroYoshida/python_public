"""
# MJD to Date

date.py

<p.35> LIST 2-2

INPUT | mjd
OUT   | date[yy,mm,dd]

date=MjdToDate(mjd)
"""
from mjd import ModifiedJulianDay 
 
def MjdToDate(mjd):

	days = [31,28,31,30,31,30,31,31,30,31,30,31]

	jj = mjd

	yy = int(2.7379093e-03*mjd+1858.877)
	mm = 1
	dd = 1 

	day=ModifiedJulianDay(yy,mm,dd)

	r1 = 0
	r2 = jj - day

	if ((yy%4 == 0 and yy%100 !=0) or yy%400 == 0):
		days[1] = 29
	
	m=0
 
	while (int(r2)-r1-days[m] >= 0) :
		r1 += days[m]
		m += 1

	mm = m +1
	dd = r2-r1+1 
        
	if mm == 13 :
		yy += 1
		mm -=12

	date=[int(yy),int(mm),int(dd)]

	return date

