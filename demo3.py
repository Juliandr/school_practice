def day03():
	import math
	for i in range(-100, 7000):
		m = math.sqrt(i+100)
		n = math.sqrt(i+100+168)
		if m%1==0 and n%1==0:
			print(i)
day03()



for i in range(1,85):
	if 168 % i == 0:
		j = 168 / i
		if i > j and (i - j) % 2 == 0 and (i - j) % 2 == 0:
			m = (i + j) / 2
			n = (i - j) / 2
			x = n * n - 100
			print(x)