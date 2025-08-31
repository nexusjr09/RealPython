#Voter eligibility shower : 

age = int(input("Enter your age : "))
if age >= 18:
    print("You are eligible to vote !")
elif age < 18:
    print("You are not eligible to vote !")
elif age < 1:
    print("you are not even born lil bro")
else:
    print("Nah bro sorry next time !")

#if both the conditions are true for one input then the condition with if will be priotized 1st rather than elif and else : 

#use of if with comparison of strings 

food = input("Do you want some food (y/n) :")
if food == "y": #== is for comparison of strings and = is for number/integer 
    print("got you bro ! I will send you some ")
else :
    print("Ok g , No worry have a good day ")

#use of boolean in If/else

food_instock = "True"
if food_instock : #while using boolean you can directly use variable to compare as there is "true/false" already
    print("yes it's available you can grab some !")
else :
    print("I am sorry bro its out of stock ")

#another example 
userstatus = True 
if userstatus:
    print("he is online ")
else:
    print("He is offline")