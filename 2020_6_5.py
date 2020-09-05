username = []
passward = []
def main():
	print('*'*20 + '主界面' + '*'*20)
	print('1.用户注册')
	print('2.用户登录')
	print('3.退出')
	print('*'*45)
def get_choice():
	return int(input('请输入选择的序号：'))
def passward_check(passward):
	a = 0
	for i in passward:
		if ord(i)>=48 and ord(i)<=57:
			digit = True
		if ord(i)>=65 and ord(i)<=90:
			alpha_A = True
		if (ord(i)>=97 and ord(i) <= 122):
			alpha_a = True
	if len(passward) >= 6 and digit and alpha_a and alpha_A:
		a = 1
	return a

def register():
	username_r = input('请输入用户名')
	userpassward_r = input('请输入密码')
	while (1 - passward_check(userpassward_r)):
		userpassward_r = input('请输入密码带大写小写数字')
		print(1)
	reuserpassward = input('请再此输入密码')
	while 1:
		if userpassward_r == reuserpassward:
			username.append(username_r)
			passward.append(userpassward_r)
			break
		else:
			userpassward_r = input('请输入密码')
			if passward_check(userpassward_r):
				reuserpassward = input('请再此输入密码')

def login():
	username_l = input('请输入用户名')
	userpassward_l = input('请输入密码')
	if username_l in username:
		if passward[username.index(username_l)] == userpassward_l:
			print('登陆成功')
		else:
			print('密码错误')
	else:
		print('不存在此用户')
def exit_menu():
	return 2
i = 0
while i == 0:
	main()
	choice = get_choice()
	if choice == 1:
		register()
	elif choice == 2:
		login()
	elif choice == 3:
		i = exit_menu()
