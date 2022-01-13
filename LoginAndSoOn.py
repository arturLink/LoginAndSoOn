from module1 import *
users=["bigDaddySvin", "GreatGuy", "bunda"]
passwords=["mamasvin","GreatestGuy","ULTRAbunda228"]
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
		newAc()
		print("Congrats! You've created yourself a new account")