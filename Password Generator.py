import random
import math
# These are all stored value to generate a random password
random_letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
random_numbers=["1","2","3","4","5","6","7","8","9","0"]
random_charecters=['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

user_input_letters=int(input("How many letters would you like to have on your password?\n"))
user_input_numbers=int(input("How many numbers would you like to have on your password?\n"))
user_input_characters=int(input("How many special cheerer would you like to have on your password?\n"))

# Stored values on a form of an array:

# difficulty level : Easy
password=""
# What if user_input_letters=4
# This one is for generating letters for that password:
for character in range(1,user_input_letters+1):
    random_let=random.choice(random_letters)
    password += random_let
    # print(password)

# This portion of the code is to generate some random numbers for that password:
for numbers in range(1,user_input_numbers+1):
    random_num=random.choice(random_numbers)
    password +=random_num
    # print(password)

# This portion of the code is to create some special character randomly in order to put them onto the password:
for character in range(1,user_input_characters+1):
    random_char=random.choice(random_charecters)
    password +=random_char
    print(password)


