#weight converter 
weight = float(input("Enter your weight : "))
unit = input("Enter the unit (kg or pounds : )")
if unit == "kg":
    print(f"{weight}kg to pound is {weight*2.205} pounds")
elif unit == "pounds":
    print(f"{weight}pound to kg is {round(weight/2.205)}kg")
else:
    print("Invalid Unit !!!")
