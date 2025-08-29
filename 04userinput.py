#userinput
name = input("Enter you Name")
print(f"Your name is {name}")
age = input("enter your current age:")
 #when you enter your age its is recognized as string not integer !! so converting to int :
age = int(age)
#or it can also be directly changed without writing another line of code example :
lastyearage = int(input("enter your age"))
age = age + 1
print(f"next year your age will be {age}")
lastyearage = lastyearage - 1
print(f"last year your age was {lastyearage}")

#exercise
length = int(input("Enter the length of the rectangle"))
breadth = int(input("Enter the breadth of the rectangle"))
area = length*breadth
print(f"The area of the rectangle is {area}")
