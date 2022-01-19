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
	print(f"Your own password: {password}")#seems useless now

def passwordcheck(password):
	"""
	"""
	cond=False
	passwordChek=list(password)
	for i in passwordChek:
		if i.isupper():
			cond=True
		if i.isdigit():
			cond=True
		if i.islower():
			cond=True
	return cond

def logIncheck(username,password,users:list,passwords:list):
	"""
	"""
	condUn=True
	condPw=True
	if username not in users:
		print("Incorrect username!")
		condUn=False
	if password not in passwords:
		print("Incorrect password!")
		condPw=False
	a=len(users)
	b=len(passwords) #dorabotat
	
	if condUn and condPw:
		print("Everything is correct you may log in!")
	return condUn, condPw

def failist_lugemine(f:str,l:list):
	fail=open(f,"r") #encoding="utf-8-sig"
	for rida in fail:
		l.append(rida.strip()) #"\n"
	fail.close()
	return l

def failisse_salvestamine(f:str,l:list):
	fail=open(f,"w")
	for el in l:
		fail.write(el+"\n")
	fail.close()

def rida_salvestamine(f:str,rida:str):
	fail=open(f,"a")
	fail.write(rida+"\n")
	fail.close()