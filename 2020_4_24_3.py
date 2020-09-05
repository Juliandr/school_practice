list1=["学号","姓名","性别","年龄","英语成绩","思政成绩","Python成绩"]

list2=["201865110210","李天","男",18,90,66,85]

list3=["201865110202","赵琴","女",29,85,87]

list4=["201865110203","王一凡","男","女",20,84,79]

fix = list1[2]
list1[2] = list1[3]
list1[3] = fix

list2[0] = "201865110201"

list3[4] = 19
list3.append(88)

list4[1] = '王凡'
del list4[3]
list4.insert(4,68)
English_ever_grade = (list2[4] + list3[4] + list4[4])/3
policy_ever_grade = (list2[5] + list3[5] + list4[5])/3
python_ever_grade = (list2[6] + list3[6] + list4[6])/3
print(list1)
print(list2)
print(list3)
print('''英语成绩是：%.1f
思政平均成绩是: %.1f
python平均成绩是: %0.1f''' % (English_ever_grade,policy_ever_grade,python_ever_grade))
