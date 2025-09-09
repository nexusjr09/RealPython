#length of string 
name = input("Enter your name : ")
print(len(name))

#space line no detector
space = name.find(input("Enter letter to find : "))
print(space)

#Indexing (position) → starts from 0 (to access positions).
#Length (len())(COUNTING) → counts the total number of items (not positions). 
#MUST UNDERSTAND 

# COUNTING ---> STARTS FROM 1 
# POSITION ---> STARTS FROM 0 

#name.find----> It starts to see from right to left ! (REMEMBER : POSITION STILL REMAINS THE SAME THOUGH IT STARTS FROM BACKSIDE)
#name.rfind ----> It starts to see from Left to right ! 

name = input("Enter your name : ")
position = name.rfind(input("Enter which letter to find : "))
print(position)

#LETS LERAN ABOUT SOME FUNCTIONS
#givenvariable.capitalize() (IT CAPITALIZES THE FIRST WORD OF THE LETTER )
#givenvariable.upper()
#givenvariable.lower()
#givenvariable.isdigit() [WILL THROW TRUE IF ALL THE LETTERS ARE DIGIT ELSE FALSE ]
#givenvariable.isaplha() [IT WILL RETURN TRUE IF IT ONLY CONTAINS ALPHABET (SPACE SHOULD NOT BE THERE) ELSE IT WILL THROW FALSE]
#givevariable.count("what to count")
#givenvariable.replace("letter to be replaced","newletter to be included")

pahichan = input("Enter your full name : ")
print(pahichan.capitalize())
print(pahichan.upper())
print(pahichan.lower())
print(pahichan.isalpha())
print(pahichan.count("a"))
print(pahichan.replace("a","z"))


