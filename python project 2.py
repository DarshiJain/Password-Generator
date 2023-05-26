#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     30-04-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("WELCOME TO PASSWORD GENERATOR")
n_letters = int(input("How many letters you want in your password ?\n"))
n_numbers = int(input("How many numbers you want in your password ?\n"))
n_symbols = int(input("How many symbols you want in your password ?\n"))
password = ""
for i in range(1,n_letters+1):
    char = random.choice(letters)
    password = password + char
for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password = password + char
for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password = password + char
print(f"YOUR PASSWORD IS :{password}")



