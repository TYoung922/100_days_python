#Write your code below this line
# print("Hello " + input("What is your name? ") + "!")
# print(len(input("what is your name ")))
# time_until_midnight = ("5")
# print("There are"+time_until_midnight+" hours until midnight")
# print(type("Hello World"))
# print(type(42))
# print(type(1257.1))
# print(type(True))

# name = input("Enter your name ")
# name_length = len(name)
#
# print("Number of letters in your name: " + str(name_length))
# score = 0
# #scores a point
# score += 1
# number = input("please give me an whole number ")
# result = int(number) % 2
# if result == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# pepp = input("Do you want pepperoni on your pizza? Y or N: ")
# ext_chee = input("Do you want extra cheese? Y or N: ")
#
# if size.upper() == "S":
#     price = 15
#     if pepp.upper() == "Y":
#         price += 2
#     if ext_chee.upper() == "Y":
#         price += 1
#     print(price)
# if size.upper() == "M":
#     price = 20
#     if pepp.upper() == "Y":
#         price += 3
#     if ext_chee.upper() == "Y":
#         price += 1
#     print(price)
# if size.upper() == "L":
#     price = 25
#     if pepp.upper() == "Y":
#         price += 3
#     if ext_chee.upper() == "Y":
#         price += 1
#     print(price)

# import random
# # random_num = random.randint(1, 10)
# # print(random_num)
# random_num = random.random() * 10
# print(random_num.__round__())

# import random
# num = random.random() * 100
# side = num.__round__()
# print(side)
# if side >= 50:
#     print("Heads")
# elif side < 50:
#     print("Tails")
# else:
#     print("It landed on its side some how")

# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel", "Tyler"]
# c = random.randint(0, 5)
# print(friends[c])
# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel", "Tyler"]
# print(random.choice(friends))

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])

# def my_function():
#     print("Hello")
#     print("Bye")
#
# my_function()

# # robot game
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     # move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# def high_jump():
#     turn_left()
#     while right_is_clear() != True:
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#     while right_is_clear():
#         turn_right()
#         move()
#
#
# while at_goal() != True:
#     if front_is_clear():
#         move()
#     else:
#         high_jump()

# import random
#
# word_list = ["aardvark", 'baboon', 'camel']
#
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
# guess = input("Guess a letter: ").lower()
#
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# my_list = ['test', 'test', "apple"]
# print("test" in my_list)

# def greet(name):
#     print("Hello")
#     print("My name is:")
#     print(name)
#
# # name_me = "Tyler Young"
# greet("Tyler Young")

# def greeting(name):
#     print("Hello", name)

# #functions with more than one input
# def greet_with(name, location):
#     print("Hello", name)
#     print("How was your trip from", location)
#
# greet_with("Tyler", "Houston")

# prgramming_dictionary = {
#     "Bug": "Ann error in the code",
#     "Function": "A pice of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again",
# }
#
# # print(prgramming_dictionary)
# prgramming_dictionary["For Loop"] = "a loop that goes over everything usually in a list"
# for key in prgramming_dictionary:
#     print(key)
#     print(prgramming_dictionary[key])