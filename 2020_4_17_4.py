number = 0
zimu = 0
zifu = 0
hanzi = 0
a = '2019, 中国, china, 欢迎您!'
for i in a:
	if ord(i)>=48 and ord(i)<=57:
		number += 1
		continue
	elif (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i) <= 122):
		zimu += 1
		continue
	elif ord(i)<127:
		zifu += 1
		continue
	else:
		hanzi += 1
		continue
print(f'''字母有:{zimu}个
数字有:{number}个
字符有:{zifu}个
汉字有:{hanzi}''')
