#NESTED LOOP == A LOOP WITHIN ANOTHER LOOP (OUTER ,INNER)
#OUTER LOOP
    #INNER LOOP


#Outer loop → controls rows (how many lines to print)
#Inner loop → controls columns (what to print in each line)

horizontal = int(input("Enter how many rows to print: "))
vertical = int(input("Enter how many to print : "))
letter = input('Enter what to print : ')

for x in range(horizontal):
    for y in range(vertical):
        print(letter, end=" ")
    print()   # ✅ This moves to the next line after finishing a row so it should be inside the LOOP TO SWITCH LINES 
#whereas if you put print() statement outside like this :
#print()--->It would only act when loops gets completed and will print on same line . 