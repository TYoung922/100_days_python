print(r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
''')

noose_state = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["aardvark", "baboon", "camel", "apple", "computer", "yellow"]
word = random.choice(word_list)

reveal = list(len(word) * "_")
chosen_word = list(word)

# print("Word to guess:", ''.join(reveal))
# print(word)
correct_guess = False
win = False
life = 6
man_state = 1
previous_guess = []
already = False

if not win:
    while life > 0:
        print("Word to guess:", ''.join(reveal))
        player_guess = input("Guess a letter: ").lower()
        if player_guess in previous_guess:
           already = True
        else:
            previous_guess.append(player_guess)
        # print(previous_guess)

        if not already:
            for index, let in enumerate(chosen_word):
                if let == player_guess:
                    reveal[index] = player_guess
                    correct_guess = True

            if correct_guess:
                print(''.join(reveal))
                correct_guess = False
            else:
                life -= 1
                print(f"You guessed {player_guess}, that's not in the word. You lose a life.")
            blank_check = "_"
            if not blank_check in reveal:
                win = True
                print("You Win!")
                life = -1
            else:
                print(noose_state[life])
                print(f"******************************* {life}/6 Lives Left *******************************")
        else:
            print(f"you've already guessed {player_guess}")
            already = False
    if life == 0:
        print(f"It was {word}. You Lose!")


else:
    print("You Win!")