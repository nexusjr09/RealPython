#logical operators in PYTHON #september 08 
#or = at least one condition must be TRue 
#and = both the condition must be true to go  forward
#NOT = inverts the condition (not False , not True)

#OR OPERATOR
age = 16 
brain = 17 
physical = 18 
if age > 18 or brain > 18 or physical >= 18 :
    print("You can participate ! ")
else :
    print("Sorry you cannot participate !")

#AND OPERATOR 
age = 18 
brain = 18
physical = 14 
if age >= 18 and brain >= 18 and physical >=14 :
    print("You are invited to Participate : ")
else: 
    print("sorry but you are not eligible !")

#NOT OPERATOR
age = 19
brain = 20
physical = 22
if age>=18 and brain >=18 and not physical<=17:
    print("You are eligible : ")
elif age>15 and not brain <18 and not physical <=17 :
    print("You  are also eligible !")
else :
    print("You are not eligible ! ")

#THIS IS ALL THE LOGICAL OPEARTORS IN PYTHON 
