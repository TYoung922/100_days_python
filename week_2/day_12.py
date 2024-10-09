import random

thinking = random.randint(1,101)
difficulty = None
print("Welcome to the Number Guessing Game")
difficulty_setting = input("Choose a difficulty. 'Easy' or 'Hard'? ").lower()
if difficulty_setting == 'easy':
    difficulty = "easy"
elif difficulty_setting == 'hard':
    difficulty = "hard"

def guessing():
    life = 0
    player_guess = 0
    if difficulty == "easy":
        life = 10
    else:
        life = 5
    print(f"You have {life} attempts remaining to guess")
    while player_guess != thinking and life > 0:
        guess = int(input("Make a guess: "))
        player_guess = guess
        if guess < thinking:
            life -= 1
            print("Too low.")
            print(f"You have {life} attempts remaining;")
        elif guess > thinking:
            life -= 1
            print("Too high.")
            print(f"You have {life} attempts remaining;")
        else:
            print(f"You got it!")
    if player_guess == thinking:
        print(f"The answer was {thinking}")
    else:
        print(f"You loose. The number was {thinking}")


guessing()