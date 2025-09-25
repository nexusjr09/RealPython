foods = ["rice" , "dal", "pickle" , "achar"]
meat = ["chicken","buffalo","fish", "pigeon"]
extras = ["spoon", "scissors", "pen","copies"]

stuffs = [foods , meat , extras]
#print(stuffs[0][2]) #    FORMAT : ---> (stuffs[row][column])
#print(stuffs[2][2])

#TWO DIMENSIONAL LIST 

snacks =  [["lays", "burger","pizza"],
           ["kurkure","corndog" ,"cheetos"],
           ["momo","chowmein","noodles"]]

#print(snacks[2][1])

for snack in snacks: #it will represent single iteration at a time . and then after completing it , it will move to second iteration /second line . 
    for sna in snack:  #sna here represents whole word  not single letter . 
        print(sna,end = " ")
    print() #It means: "after finishing one round of the inner loop, move to a new line not every alphabet  will be print in new line only after completing full word 

#NUMPAD 

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))
for num in num_pad:
    for n in num:
        print(n , end = " ")
    print()