import random
a = ['石佳','陈浩拓','肖湘吉','丁庆玲','陈娅','陈雨杭','高家纯','刘腾','刘小叶','唐志荣','倪思理','周子涵']
a_group = []
b_group = []
c_group = []
for i in range(3):
	num = random.randint(0,len(a) - 1)
	a_group.append(a[num])
	del a[num]
for i in range(3):
	num = random.randint(0,len(a) - 1)
	b_group.append(a[num])
	del a[num]
for i in range(3):
	num = random.randint(0,len(a) - 1)
	c_group.append(a[num])
	del a[num]
print(a_group)
print(b_group)
print(c_group)

