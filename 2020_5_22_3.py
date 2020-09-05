day_nov_two_four = {'牛奶':15,'方便面':25,'糖果':10}
day_nov_two_five = {'牛奶':15,'咖啡':5,'饼干':15,'火腿肠':10}
day_nov_two_six = {'奶茶':10,'牛奶':20,'方便面':15}
stuffS_price = {'牛奶':5.5,'方便面':4,'糖果':12,'咖啡':6,'饼干':6,'火腿肠':5,'奶茶':5}
print('11月24日')
goods_earn = 0
sold_out = 0
for key,value in day_nov_two_four.items():
	print("\t%s:\t\t数量:%d\t\t单价:%d"%(key,value,stuffS_price[key]))
	sold_out += value
	goods_earn += value*stuffS_price[key]
print(f'11月24日卖出货物{sold_out}件,小计:{goods_earn}元')
print('11月25日')
goods_earn = 0
sold_out = 0
for key,value in day_nov_two_five.items():
	print("\t%s:\t\t数量:%d\t\t单价:%d"%(key,value,stuffS_price[key]))
	sold_out += value
	goods_earn += value*stuffS_price[key]
print(f'11月25日卖出货物{sold_out}件,小计:{goods_earn}元')
print('11月26日')
goods_earn = 0
sold_out = 0
for key,value in day_nov_two_six.items():
	print("\t%s:\t\t数量:%d\t\t单价:%d"%(key,value,stuffS_price[key]))
	sold_out += value
	goods_earn += value*stuffS_price[key]
print(f'11月26日卖出货物{sold_out}件,小计:{goods_earn}元')
