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
		print(f"You own password: {password}") #rabotaet no ne dokontsa

def passwordcheck(password):
	"""
	"""
	[]#spisk dlja znakov
	if (password.isupper()) and (password.isdigit()) and (password.islower()) and password in []#znaki