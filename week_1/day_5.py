import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# mine
lett = []
while nr_letters > lett.__len__():
    lett.append(letters[random.randint(0, letters.__len__() - 1)])
sym = []
while nr_symbols > sym.__len__():
    sym.append(symbols[random.randint(0, symbols.__len__() - 1)])
numb = []
while nr_numbers > len(numb):
    numb.append(numbers[random.randint(0, len(numbers) - 1)])

password = lett + sym + numb
random.shuffle(password)
print(password)
random.shuffle(password)
print(password)
#
result_pass = ''.join(password)
print("Your password is: ", result_pass)

# #there result easy
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

# there result hard
# password_list = []
# for char in range(0, nr_letters):
#     password_list.append(random.choice(letters))
#
# for char in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))
#
# for char in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#     password += char
#
# print(f"Your password is: {password}")