def factor(n):
	factor_number = []
	for i in range(1, n + 1):
		if n % i == 0:
			factor_number.append(i)
	return factor_number
array = {}
for i in range(1, 100):
	array[i] = factor(i)
print(array)


	