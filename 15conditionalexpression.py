#conditional expression 
#WITH THIS PRINT OR ASSIGN ONE OF TWO VALUES BASED ON A CONDITION 

active = True
print("He is active" if active else "He is not active")

num = 7 
print("It is even number" if num % 2 == 0  else "It is odd number")

#MAIN DIFF : == --> it is used to compare the value / check the value whereas = is to store the value 

num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
print("Num1 is greater than num2 " if num1 > num2 else "Num2 is greater than Num1 ")

temp = float(input("Enter the temperature of your Area : "))
print("It is hot " if temp > 25 else "It is Normal ")


role = "admin"
print("Access granted " if role == "admin" else "Access denied : ")
