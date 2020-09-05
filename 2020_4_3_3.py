import random
player_guess = int(input("请你输入你猜的数字（1-10之间）"))
random_int = random.randint(1,10)
count = 0
print(random_int)
while player_guess != random_int:
	count += 1
	if player_guess > random_int:
		player_guess = int(input("请你再输入小一点的数字（1-10之间）"))
	else:
		player_guess = int(input("请你再输入大一点的数字（1-10之间）"))

	
if count < 2:
	print("你太棒了!!!")
elif count < 4:
	print("恭喜你猜对了！")
elif count < 6:
	print("终于猜出来了！")
else:
	print("你太笨了游戏结束")