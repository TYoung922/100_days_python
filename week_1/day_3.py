print(r'''
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_answer = input("you're at a cross road. where do you want to go? \nType 'left' or 'right' \n").lower()

if first_answer == "left":
    print("\nYou've come to a lake. There is an island in the middle of the lake.")
    second_answer = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()


    if second_answer == "wait":
        print("\nyou arrive at the island unharmed. There is a house with 3 doors.")
        third_answer = input("One red, one yellow and one blue. Which colour do you choose? \n").lower()

        if third_answer == "red":
            print("\nFire shoots from the door burning you. \n Game Over!")
        elif third_answer == "blue":
            print("\nYou are Eaten by beasts. \n Game Over!")
        elif third_answer == "yellow":
            print("\nYou enter a room full of treasure. \n There are probably no mimics... \n YOU WIN!!")
    elif second_answer == "swim":
        print("\nAs you are swimming towards the island you see something sparkling deep in the water")
        swim_answer = input("Type 'dive' to swim down and investigate or 'ignore' to keep swimming to the island? \n").lower()
        if swim_answer == "dive":
            print("\nYou find a strange looking glass orb that glows slightly.")
            dive_answer = input("Type 'grab' to pick up the orb or type 'leave' to ignore the orb and swim back up\n").lower()
            if dive_answer == "leave":
                print("\nyou reach the surface but the island is gone")
                surface_answer = input("Type 'try' to try and swim to where the island was or 'back' to swim back to shore\n").lower()
                if surface_answer == "back":
                    print("\nYou reach the shore safely, but feel that something was lost \n you head home without any treasure,"
                          "but at least you're alive. \n Game Over.")
                else:
                    print("\nAs you get to where the island had been you realize the shore is gone too. \n"
                          "you try to search for it but are unable to find the land again and eventually drown. \n"
                          "Game Over!")
            else:
                print("\nYou grab the orb and heave upward finding that a strange tentacle is attached to the orb. \n"
                      "Out of the sand comes an enormous fish with huge pointed teeth the orb and tentacle attached to its head. \n"
                      "The fish eats you \n Game Over!")
        else:
            print("\nyou arrive at the island unharmed. There is a house with 3 doors.")
            door_answer = input("One red, one yellow and one blue. Which colour do you choose? \n").lower()

            if door_answer == "red":
                print("\nFire shoots from the door burning you. \n Game Over!")
            elif door_answer == "blue":
                print("\nA swarm of wild beasts emerge quickly devouring you. \n Game Over!")
            elif door_answer == "yellow":
                print("\nYou enter an empty room. \n As you look around you hear a loud clinking sound above you \n"
                      "You look up to see a giant treasure chest tipping to dump its contents. \n"
                      "You try to flee but aren't quick enough. The treasure crushes you.  \n Game Over!")
else:
    print("\nYou find some old ruins")
    right_one = input("Type 'in' to investigate the ruins or type 'continue' to keep searching\n").lower()
    if right_one == "in":
        print("\nThe ruins look ancient most of the wooden doors are rotted away. \n"
              "You find a door that is still intact, though barely. It won't open")
        right_two = input("Type 'bash' to attempt to bash the door open or type 'move on' to look elsewhere\n").lower()
        if right_two == "bash":
            print("\nYou take a running start and throwing your shoulder against the door bust through it in a shower of splinters. \n"
                  "Inside is a single treasure chest that has miraculously withstood the march of time.")
            right_three = input("Type 'open' to open the treasure chest or type 'leave' to leave the chest and continue searching\n").lower()
            if right_three == "open":
                print("You open the chest to see rows of gleaming pointed teeth within. \nYou are eaten by the mimic. \nGame over!")
            else:
                print("\nAs you look around your mind wonders if you should have opened the chest after all.\n"
                      "Distracted you fail to notice the giant spider web.\n"
                      "stuck in the spider's web you are unable to get away as the spider wraps you up.\n Game Over!")
        else:
            print("\nYou find nothing else in the ruins and decide to leave.\n"
                  "As you exit out the front a loose stone gives way and you topple over the railing into the chasm below\nGame Over!")
    else:
        print("\nYou find a dragon's nest with large gleaming eggs inside.")
        dragon_one = input("Type 'take' to go take an egg or type 'leave' to keep going.\n").lower()
        if dragon_one == "leave":
            print("\nYou come to a large mountain. As you look up something gleams brightly catching the light")
            dragon_two = input("Type 'climb' to climb the mountain towards the gleam or type 'leave' to move on.\n").lower()
            if dragon_two == "climb":
                print("\nAs you climb upward the air quickly grows cold. Your fingers grow numb and you loose your grip galling to your death.\n"
                      "Game Over!")
            else:
                print("\nEverything on this adventure seems far to dangerous you decide to head home.\n"
                      "You gained no treasure but kept your life.\n"
                      "Game Over.")
        else:
            print("The egg is extremely heavy.\n"
                  "As you try to cart it off the dragon returns. Hoping to get away you drop the egg and run.\n"
                  "The egg cracks leaking goop causing you to slip. Lying prone on the ground you watch in horror\n"
                  "as gleaming teeth come for you.\n"
                  "Game Over!")