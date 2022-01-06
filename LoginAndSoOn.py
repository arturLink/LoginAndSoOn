from module1 import *
user1="bigDaddySvin"
user2="GreatGuy"
user3="bunda"
users=[user1, user2, user3]
password1=("mamasvin")
password2=("GreatestGuy")
password3=("ULTRAbunda228")
print("Hello!")
print("To access the application you need to register")
answer=int(input("Do you want to? 1 for Yes, 2 for No: "))
while 1:
	if answer==1:
		print("Great!")
	elif answer==2:
		print("Sad...")
		print("You may exit the programm, by typping 'exit' or you can register by typping 'reg'")
		a=input("")
		if a=="exit":
			break