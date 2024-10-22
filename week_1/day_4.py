import random

player = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n"))
computer = random.randint(0, 2)
rock = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """
paper = """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """
scissors = """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """

if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)

print("Computer chose:")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

if player == 0 and computer == 0:
    print("It's a tie.")
elif player == 1 and computer == 0:
    print("You Win!")
elif player == 2 and computer == 0:
    print("Computer Wins")

if player == 0 and computer == 1:
    print("Computer Wins.")
elif player == 1 and computer == 1:
    print("It's A Tie")
elif player == 2 and computer == 1:
    print("You Win!")

if player == 0 and computer == 2:
    print("You Win.")
elif player == 1 and computer == 2:
    print("Computer Wins.")
elif player == 2 and computer == 2:
    print("It's A Tie")