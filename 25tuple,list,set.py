# collection = single "variable" that holds multiple Values
# List = [] ordered and changeable. Duplicates OK 
# Set = {}
#Tuple = ()

fruits = ["apple","banana","grapes","Orange"]
print(fruits[0]) #number inside []will display the fruit acc to it 
print(fruits[0:3])
print(fruits[::2])
print(fruits[::-1])

#checking if value is within the list or not .
print("apple" in fruits)

#changing values from the list : 
fruits[0] = "pineapple"
print(fruits)

#adding values to the list :
fruits.append("jomsomapple")
print(fruits)

#removing values from the list:
fruits.remove("banana")
print(fruits)

#adding values to the exact position :
fruits.insert(0,"coconut")
print(fruits)

#sorting values alphabetically : 
fruits.sort()

#indexing the values
print(fruits.index("grapes"))

#counting the values in the list 
print(fruits.count("banana"))