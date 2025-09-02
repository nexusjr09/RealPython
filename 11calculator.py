#caculator 
operator = input("Enter what you wanna do : (Addition , Substraction , Divison , Multiplication )")
num1 = float(input("Enter the 1st number : "))
num2 = float(input("Enter the 2nd number : "))
if operator == "Addition":
    print(f"The addition between the two number is {num1 + num2}")
elif operator == "Substraction":
    print(f"The Substraction between the two number is {num1 - num2}")
elif operator == "Divison":
    print(f"The divison between two number is {num1 / num2 }")
elif operator == "Multiplication":
    print(f"The multiplication between two number is {num1 * num2 }")
else :
    print(f"{operator} is not a valid Operator !")

#code clean !