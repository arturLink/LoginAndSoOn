from module1 import *
users=[]
users=failist_lugemine("users.txt",users)
passwords=[]
passwords=failist_lugemine("passwords.txt",passwords)
print("Hello!")
print("To access the application you need to log in")
while 1:
	answer=int(input("Do you have an account? 1 for Yes, 2 for No: "))
	if answer==1:
		print("Great! Lets log in")
		un=input("Enter your username: ")
		pw=input("Enter your password: ")
		u,p=logIncheck(un,pw,users,passwords)

	elif answer==2:
		print("Allright, Lets create one!")
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
	print("Congrats! You've created yourself a new account")
	rida_salvestamine("users.txt",name)
	rida_salvestamine("passwords.txt",password)