str1="数据分析师,金融数据分析助理；链家数据分析员,数据分析测评工程师。数据统计分析专员"

str2="福建省三福百货有限公司;深圳市洋葱电子商务有限公司,广州市链家房地产代理有限公司,广州固诚信息咨询服务有限公司,广州思迈特软件有限公司"

str3="10000,6000,8000,8000,12000"

str1 = str1.replace(',' , ' ')
str1 = str1.replace('；' , ' ')
str1 = str1.replace('。' , ' ')
str2 = str2.replace(',' , ' ')
str2 = str2.replace(';' , ' ')
str3 = str3.replace(',' , ' ')
s = str1.split(' ')
b = str2.split(' ')
c = str3.split(' ')
sum = 0
for i in c:
	sum += int(i)
s = tuple(s)
b = tuple(b)
c = tuple(c)
print(s)
print(b)
print(c)
print("他们的平均工资是",end = ':')
print(sum/5)

