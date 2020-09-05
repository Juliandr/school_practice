def display_menu():
    print("-------------------------\n"
       "\t名片管理系统\tV1.0\n"
       "1.添加名片\n"
       "2.查询名片\n"
       "3.修改名片\n"
       "4,删除名片\n"
       "5,获取所有名片信息\n"
       "6,退出系统\n"
       "-----------------------------")


def get_choice():
	key = int(input("请输入您的xuanze："))
    return key
def add_info():
	name = input('请输入姓名：')
	work = input('请输入工作：')
	ad = input('请输入地址：')
	card_dict[name] = [work, ad]

def del_info():
	name = input('请输入姓名：')
	del card_dict[name]

def revise_info():
	name = input('请输入姓名：')
	_choice = input('修改职位按1，地址按2')
	if _choice:
		card_dict[name][0] = input()
	else:
		card_dict[name][1] = input()

def seek_info():
	name = input('请输入姓名：')
	print('姓名:%s'%(name))
	print('工作:%s'%(card_dict[name][0]))
	print('地址:%s'%(card_dict[name][1]))

def print_all_info():
	for i in card_dict:
		print('姓名:%s'%(i))
		print('工作:%s'%(card_dict[i][0]))
		print('地址:%s'%(card_dict[i][1]))


def exit_menu():
	return 2

i = 0 
card_dict = {}
while i < 1:
	display_menu()
	key = get_choice()
	if key == 1:
		add_info()
	elif key == 2:
		del_info()
	elif key == 3:
		revise_info()
	elif key == 4:
		seek_info()
	elif key == 5:
		print_all_info()
	elif key == 6:
		i = exit_menu()
	else:
		print('输入错误请重新输入...')