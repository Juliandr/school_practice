# def hnt(n,a,b,c):
# 	if n == 1:
# 		print("直接将编号为%d的盘子从%s柱子移动到%s柱子上"%(n,a,c))
# 	else:
# 		hnt(n-1,a,c,b)
# 		print("将第%d的盘子从%s柱子移动到%s柱子上"%(n,a,c))
# 		hnt(n-1,b,a,c)
# hnt(10,'a','b','c')
def ok(a):
	sum = 0
	for i in a:
		sum += int(i)
	return sum
a = '360111199911232118'
print(ok(a))