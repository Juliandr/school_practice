array_number = "ixo678"
password = []
for i in array_number:
	b = ord(i) - 5
	password.append(chr(b))
for i in range(6):
	print(password[i],end='')

