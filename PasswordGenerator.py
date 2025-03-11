import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter_ = int(input("Enter the number of letter do you want \n"))
numbers_ = int(input("Enter the number of number do you want\n "))
symbols_ = int(input("Enter the number of symbols do you want \n"))

password_list =  []


for char in range(1,letter_+1):
    password_list.append(random.choice(letters))
for char in range(1, numbers_ + 1):
    password_list.append( random.choice(numbers))
for char in range(1, symbols_ + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)


password = ""
for item in password_list:
    password += item

print("YOUR FINAL PASSWORD IS READY IT IS ")
print(f"{password}")
