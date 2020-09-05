renmingbi = 100
for i in range(20):
	for j in range(33):
		if i * 5 + j * 3 + (100 - i - j)/3 == 100 and (100 - i - j) % 3 == 0:
			print(f"公鸡是{i}只，母鸡是{j}只，小鸡是{100 - i - j}只")
			#第一组彭玉龙