from module1 import *
["bigDaddySvin", "GreatGuy", "bunda"]
["mamasvin","GreatestGuy","ULTRAbunda228"]
print("Hello!")
print("To access the application you need to log in")
answer=int(input("Do you have an account? 1 for Yes, 2 for No: "))
while 1:
	if answer==1:
		print("Great! Lets log in")
		logIn()
		print("Congrats! You've logged in!")
	elif answer==2:
		print("Allright, Lets create one!")
		newAc()
		print("Congrats! You've created yourself a new account")