#shopping cart program
item = input("What item would you like to buy from us : ")
price = float(input("What is the price of the item you  picked : "))
quantity = int(input("How many do you want ? : "))
total = price*quantity
print(f"Thank you for purchasing . Your total amount to be paid is  ${total} ")