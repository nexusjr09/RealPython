#format specifiers
price1 = 120.99
price2 = 45.67
price3 = 67.89

#helps in getting required digits after decimal using specifiers !

print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.1f}")

data1 = float(input("Enter the 1st data : "))
data2 = float(input("Enter the 2nd data : "))
data3 = float(input("Enter the 3rd data : "))
print(f"Data 1 is : {data1:.3f}")
print(f"Data 2 is : {data2:.2f}")
print(f"Data 3 is : {data3:.1f}")

#with this you can create your space for output
print(f"Checking for Space : {price1:10}") #----> Creates 10 spaces for output
