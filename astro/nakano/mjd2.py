def cal_mjd(mn,dy,yr):

	m = mn

	if yr <0 :
		yr += 1
	y =yr

	if mn < 3:
	   	m += 12
		y -=  1
	
	if (yr <1582 or (yr ==1582 and (mn < 10 or (mn == 10 and dy <15 )))):
		b = 0
	else :
		a = y/100
		b = 2 - a + a/4

	if y<0 :
		c = int(365.25*y-0.75) - 694025
	else :
		c = int(365.25*y)- 694025
	
	d = int(30.6001*(m+1))

	mjd = b + c + d + dy - 0.5
	
	return mjd

