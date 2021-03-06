from datetime import datetime

def date_jd(to_jd):
	date_time = datetime.strptime(to_jd, '%Y-%m-%dT%H:%M')
	
	y = date_time.year
	m = date_time.month
	d = date_time.day
	h = date_time.hour
	mm = date_time.minute
	ss = date_time.second
	
	if m == 1 or m == 2:
		y = y-1
		m = m+12

	A  = int(y/100)
	B  = 2 - A + int(A/4)
	C  = int(365.25*y)
	D  = int(30.6001*(m+1))
	dd = d + (h/float(24)) + (mm/float(1440)) + (ss/float(86400))

	jd = B +C + D + dd + 1720994.5

	return jd

def jd_date(to_jd):
	I = int(to_jd + 0.5)
	F = to_jd + 0.5 - I
	A = int((I - 1867216.25)/36524.25)
	B = I + 1 + A - int(A/4)
	C = B + 1524
	D = int((C - 122.1)/365.25)
	E = int(365.25*D)
	G = int((C - E)/30.6001)
	d = C - E + F - int(30.6001*G)

	if G < 13.5:
		m = G - 1
	else:
		m = G - 13

	if m > 2.5:
		y = D - 4716
	else:
		y = D - 4715

	hour = (d - int(d))*24
	min = (hour - int(hour))*60
	sec = (min - int(min))*60

	return "%(m)i/%(d)i/%(y)i, %(hour)i:%(min)i:%(sec)i" %locals()
