#indexing = accessing elements of a sequence using []

number = "9824-012-184" #starts from 0 and includes the character that is in 0 but it doesn't include the character of the ending index
print(number[0:5])

name = "bigyanbaral"
print(name[0: 5]) #The character in 0 position is counted but not the last one 

credit_card = "078-0999-6789"
print(credit_card[0:]) #if we don't add anything in the end python assumes that the user want's everything to be printed

print(credit_card[-1])
print(credit_card[-3])
print(credit_card[-2]) #this means we can also use string slicing/indexing using negative numbers that counts  from reverse 