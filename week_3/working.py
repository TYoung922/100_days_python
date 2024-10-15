# snake = Turtle("square")
# snake.color('white')
# snake2 = Turtle("square")
# snake2.color("white")
# snake.forward(20)
# snake3 = Turtle("square")
# snake3.color("white")
# snake2.back(20)

# segment_1 = Turtle("square")
# segment_1.color("white")
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater.")
#
#     def swim(self):
#         print("moving in water")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)

# def add(*num):
#     sum_of = 0
#     for n in num:
#         sum_of += n
#
#     print(sum_of)
#
# add(1, 2, 3, 3)

# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)

# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
# my_car = Car(make="nissan", model="gt-r")
# print(my_car)

i = 1
while i <= 10:
   print(i * '*')
   i = i + 1