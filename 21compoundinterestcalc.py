#COMPOUND INTEREST CALCULATOR !!!!!
principle = int(input("Enter principle amount : "))
while principle <=0:
    print("Principle cannot be 0 or less than 0 !")
    principle = int(input("Enter Principle Amount: "))

rate = float(input("Enter the Interest Rate : "))
while rate <=0 :
    print("Rate cannot 0 or less than Zero : ")
    rate = float(input("Enter the Rate : "))

time = int(input("Enter the no of months you want to apply interest : "))
while time <=0:
    print("Time cannot be Zero or less than Zero . Enter valid no of Months : ")
    time = int(input("Enter the no of Months : "))

total_balance = principle * ((1 + rate/100)**(time/12)) #time/12 means converting in year ! 
print(f"Your total balance after {time} months will be {total_balance:.2f} ! ")

