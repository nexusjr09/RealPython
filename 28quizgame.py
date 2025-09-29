#quiz game 

questions = ("1. Who is the current Prime minister of Nepal ? " ,
             "2. Who is current Education Minister Of Nepal ? ",
             "3. Who is Mayor of Kathmandu ? ",
             "4. Who was the EX prime minister of Nepal ? ",
             "5. Out of 14 highest Peak in the world , How many are located in Nepal ? ")

options = (("A. Harka Sampang", "B. Balen Shah", "C. Sushila Karki", "D. Sagar Dhakal "),
           ("A. Ma,habir Pun", "B. Sumana Shrestha", "C. Rabi Lamichhane", "D. Nexus Code"),
           ("A. Kp Oli ", "B. Balen Shah", "C. Sisan Baniya", "D. Shrinkhala Khatiwada"),
           ("A. SherBahadur Deuba", "B. Pushpa Kamal Dahal", "C. KP Sharma Oli", "D. Ramchandra Poudel"),
           ("A. 7", "B. 9" , "C. 10" , "D. 8"))

answers = ("C" ,"A", "B" , "C" , "D")
guesses = []
score = 0 
question_num = 0 

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter the answer  (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score = score + 1 
        print("Correct ! ")
    else:
        print("Incorrect !")
        print(f"The correct answer is {answers[question_num]}")
    question_num = question_num + 1

print("--------------------")
print("    RESULT         ")
print('---------------------')
print("answers: ", end = " ")
for answer in answers:
    print(answer, end = " ")
print()
print("guesses: ", end = " ")
for guess in guesses:
    print(guess , end  = " ")
print()

print(f"Your total score is : {score}")
