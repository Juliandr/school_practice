sum_a =input('需要加法的数，空号隔开:')
a = sum_a.split(' ')
sum_all = 0
for i in a:
	sum_all += int(i)
print(f'之和为{sum_all}')
