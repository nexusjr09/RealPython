#strings only 
first_name = "Nexus"
last_name = "Junior"
print(first_name)
print(last_name)
print(f"My name is {first_name} {last_name}")

#integers (only whole numbers and should be not included inside double "" else it will be considered as string.)
age = 17
print(f"My age is {age}")
quantity = 7 
print(f"{first_name} {last_name} is {age} years old and has brought {quantity} chocolates")

#float ( number with decimal portion)
price = 15.99
gpa= 3.56 
distance = 10.7 
print(f"The price of the biscuit is NPR {price} ")
print(f"My GPA on class 12 was {gpa}")
print(f"My distance between house and school is {distance}km")

#boolean (True or False)
nepali = False
if nepali:
    print("timi Nepali raixau")
else:
    print("YOu are not a Nepali")

on_sale = True
if on_sale:
    print("yes this is available for sale")
else:
    print("This items are not listed for sale")

#FINAL PROJECT USING ALL THE VARIABLES ::::::

name = "Bigyan"
money = 7500
salary = 5520.5
rich = True 

print(f"My name is {name} I have {money} in my bank account")
print(f"Currently my salary is{salary} .")
if rich:
    print("and yes I am happy to say I am definitely rich")
else:
    print("Unfortunately I am not a rich person")