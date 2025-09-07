#Temperature conversion 
temp = float(input("Enter the temperature : "))
unit = input("Is the Temperature on Celsius or Kelvin : ")
if unit == "Celsius" or "celsius" or "CELSIUS":
    print(f"{temp} Celsius to Kelvin is {(temp+273)} Kelvin")
elif unit == "Kelvin" or "KELVIN" or "kelvin":
    print(f"{temp} kelvin to celsius is {temp-273}° Celsius ")
else :
    print("Invalid Unit ! ")
