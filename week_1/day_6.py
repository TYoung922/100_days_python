# code to make Reeborg's World work
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def priority():
    if front_is_clear():
        move()
    if right_is_clear():
        turn_right()
    else:
        turn_left()


while at_goal() != True:
    priority()


# # There way
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()