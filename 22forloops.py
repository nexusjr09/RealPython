#FOR LOOPS ----> executes a block of code for fixed number of times . 

for x in range(1,11):
    print(x)

print("Ok done ")

for x in reversed(range(1,7,2)):
    print(x)

credit = input("Enter your credit card no : ")
for x in credit:
    print(x)

for x in range(1,11):
  if x == 13:
      continue
  else:
      print(x)
