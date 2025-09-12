#WHILE LOOPS IN PYTHON  ---> EXECUTES A CODE UNTIL A CONDITION IS MET/GETS TRUE !
name = input("Enter your username : ")
while name == "":
    print("You forget to enter your name : ")
    name = input("Enter your name : ") #---> IF THIS LINE IS NOT ADDDED THEN YOU WILL ENTER IN A LOOP THAT WILL ONLY DISPLAY THE PRINT STATEMENT INFINITE TIMES

print(f"your name is {name}")

age = int(input("Enter your age : "))
while age<0:
    print("Age cannot Be Negative , Please Enter valid Age : ")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

