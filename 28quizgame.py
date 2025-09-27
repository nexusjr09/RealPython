#quiz game 

questions = ("1. Who is the current Prime minister of Nepal ? " ,
             "2. Who is current Education Minister Of Nepal ? ",
             "3. Who is Mayor of Kathmandu ? ",
             "4. Who was the EX prime minister of Nepal ? ",
             "5. Out of 14 highest Peak in the world , How many are located in Nepal ? ")

options = (("A. Harka Sampang", "B. Balen Shah", "C. Sushila Karki", "D. Sagar Dhakal "),
           ("A. Mahabir Pun", "B. Sumana Shrestha", "C. Rabi Lamichhane", "D. Nexus Code"),
           ("A. Kp Oli ", "B. Balen Shah", "C. Sisan Baniya", "D. Shrinkhala Khatiwada"),
           ("A. SherBahadur Deuba", "B. Pushpa Kamal Dahal", "C. KP Sharma Oli", "D. Ramchandra Poudel"),
           ("A. 7", "B. 9" , "C. 10" , "D. 8"))

answers = (" C" ," A ", " B" , "C" , " D ")
guesses = []
score = 0 
question_num = 0 

for question in questions:
    print("-----------------")
    print(question)
    for option in options:
        print(option)
   
