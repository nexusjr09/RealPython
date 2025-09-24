# collection = single "variable" that holds multiple Values
# List = [] ordered and changeable. Duplicates OK 
# Set = {} unordered and immutable ,but add/remove is ok. No duplicates     
#Tuple = () ordered and uchangeable. DUPLICATES ARE OK and is much faster . 

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

#NOW LETS TALK ABOUT SET {}

vechile = {"car","truck","bus","bike"}
#in set we can only add / remove but cannot add same value twice, meaning if there are two values also then it will only display 1
#OTHERS ALL ARE SAME AS ABOVE SAME FUNCTION WE USE ON LIST IS USED ON SET

#LETS TALK ABOUT TUPLE ()

vechile = ("car","bus","truck","bikes")

#it is written in this format and other same function are used as in all this collection . we will deep dive more in projects to understand about this more . 

