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

for snack in snacks:
    for sna in snack:
        print(sna,end = " ")
    print() #It means: "after finishing one round of the inner loop, move to a new line."
