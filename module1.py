import random
def autpass():
	"""
	"""
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper()
	#print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
	str4 = str0+str1+str2+str3
	#print(str4)
	ls = list(str4)
	#print(ls)
	random.shuffle(ls)
	#print(ls)
	# Извлекаем из списка 12 произвольных значений
	psword = ''.join([random.choice(ls) for x in range(12)])
	# Пароль готов
	return psword

def newAc():
	"""
	"""
	name=input("Enter your new username: ")
	print(f"Hello, {name}!")
	print("Do you wish to randomly generate your password, or create one yourself?")
	print("'generated' or 'create my own'")
	choice=input()
	if choice=="generated":
		password=autpass()
		print(f"Your generated password: {password}")
	elif choice=="create my own":
		password=input("Enter your new password: ")
		a=passwordcheck(password)
		while a==False:
			print("Your password must contain numbers, lower cases and upper cases!")
			password=input("Enter your new password: ")
			a=passwordcheck(password)
			if a==True:
				break
	print(f"Your own password: {password}")

def passwordcheck(password)->bool:
	"""
	"""
	cond=0
	passwordChek=list(password)
	for i in passwordChek:
		if i.isupper() and i.isdigit() and i.islower() and i.islapha():
			cond=True
		else:
			cond=False
	return cond#dorabotat

def logIn():
	"""
	"""
	un=input("Enter your username: ")
	print(f"Hello, {un}!")
	pw=input("Enter your password: ")
	a=logIncheck(un,pw)
	while a==0:
		print("Either username was incorrect or password. Try again")
		un=input("Enter your username: ")
		print(f"Hello, {un}!")
		pw=input("Enter your password: ")
		a=logIncheck(un,pw)
		if a==True:
			break

def logIncheck(username,password)->bool:
	"""
	"""
	condUn=0
	condPw=0
	users=["bigDaddySvin", "GreatGuy", "bunda"]
	passwords=["mamasvin","GreatestGuy","ULTRAbunda228"]
	if username not in users:
		print("Incorrect username!")
		condUn=False
	else:
		True
	if password not in passwords:
		print("Incorrect password!")
		condPw=False
	else:
		True
	return condUn and condPw#dorabotat