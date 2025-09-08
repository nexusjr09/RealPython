#Temperature conversion 
temp = float(input("Enter the temperature : "))
unit = input("Is the Temperature on Celsius or Kelvin : ")
if unit == "Celsius":
    print(f"{temp} Celsius to Kelvin is {(temp+273)} Kelvin")
elif unit == "Kelvin":
    print(f"{temp} kelvin to celsius is {temp-273}° Celsius ")
else :
    print("Invalid Unit ! ")
