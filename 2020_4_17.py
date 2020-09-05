student_identify = input('输入宁的学号：')
internet_source_divison = student_identify[4:8]
is_internet_source_divison = (internet_source_divison == '6511')
while len(student_identify) != 12:
	print('宁输入的学号不对，请重新输入：',end=' ')
	student_identify = input()
if is_internet_source_divison:
 	print(f"学号为{student_identify}的学生是网络资源部门的学生")
else:
 	print('你是学生')
