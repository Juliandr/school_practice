id_card = input('请输入你的身份证号码：')
id_card_secret = id_card[:-8] + '****'+ id_card[-4:]
province_check = id_card[:2]
birth_day = id_card[6:14]
gender = id_card[16]
print('-'*30)
print("该人的身份信息如下：")
if province_check == '43':
	print("所在省份：湖南省")
print('出生日期：' + birth_day)
if int(gender)%2 == 0:
	print("性别：女")
else:
	print("性别：男")
print('-'*30)
print('身份证保密显示如下：'+id_card_secret)