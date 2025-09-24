#SHOPPING CART PROGRAM 
foods =[]
prices = []
total = 0
while True:
    food = input("Enter food to purchase  ( press q to quit) : ")
    if food == "q" or food =="Q": #alternative line : food.lower() ="q" ---> food.lower() will automatically take input in lower case even if it is input as uppercase
       break
    else:
        price = float(input("Enter the price of the food in $ : "))
        foods.append(food)
        prices.append(price)
print("------ YOUR TOTAL FOODS IN YOUR CART : ---------")
for food in foods:
    print(food,end = " ")
for price in prices:
    total = total + price
    print() #this is added to display the total amount just below the cart
print(f"Your total amount is ${total}")