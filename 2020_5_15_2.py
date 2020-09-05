b = {'牛奶':65,'面包':15,'可乐':39,'饼干':45,'糖果':24,'水果':38.5}
b['牛奶'] = 60
sum = 0
for value in b.values():
	sum += value
print(b)
print(f"您购买6件物品，共计：{sum}元")
