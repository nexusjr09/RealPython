#exercise and following rules should be followed :
#1) Username should not contain more than 12 Characters ! 
#2) It should not contain digits in it !
#3) It should not have spaces in it !

user_name = input("Enter the username : ")
length = len(user_name)
space = user_name.find(" ")
data = user_name.isalpha()

if length > 12 :
    print("Username shouldn't contain More than 12 characters !")
elif not space == -1 : 
    print("Username should not contain Space inside it ! ")
elif  data == False :
    print("Username shouldn't contain Digits in it !")
