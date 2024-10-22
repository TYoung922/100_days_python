import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
player_score = sum(player_hand)
dealer_score = sum(dealer_hand)
player_busted = False

def calculate_player():
    global player_score
    player_score = sum(player_hand)
    if 11 in player_hand and player_score > 21:
        player_hand[player_hand.index(11)] = 1
        player_score = sum(player_hand)

def calculate_dealer():
    global dealer_score
    dealer_score = sum(dealer_hand)
    if 11 in dealer_hand and dealer_score > 21:
        dealer_hand[dealer_hand.index(11)] = 1
        dealer_score = sum(dealer_hand)


def player_draw():
    calculate_player()
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer first card: {dealer_hand[0]}")
    continue_on = input("Type 'y' to get another card, or 'n' to stand: ").lower()
    if continue_on == 'y':
        player_hand.append(cards[random.randint(0, 12)])
        calculate_player()
        if player_score == 21:
            finish_game()
        elif player_score < 22:
            player_draw()
        else:
            global player_busted
            finish_game()
            player_busted = True
    else:
        finish_game()

def play_blackjack():
    player_hand.append(cards[random.randint(0, 12)])
    player_hand.append(cards[random.randint(0, 12)])
    dealer_hand.append(cards[random.randint(0, 12)])
    dealer_hand.append(cards[random.randint(0, 12)])
    player_draw()



def dealer_draw():
    calculate_dealer()
    while dealer_score < 17:  # Keep drawing until dealer's score is 17 or more
        dealer_hand.append(cards[random.randint(0, 12)])
        calculate_dealer()  # Update dealer's score after drawing
    finish_game()


def finish_game():
    global player_busted
    calculate_player()
    calculate_dealer()
    if dealer_score < 17:
        dealer_draw()

    if player_busted:
        print(f"You busted with {player_hand} score: {player_score}")
        print(f"Dealer had a hand with {dealer_hand} score: {dealer_score}")
    else:
        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

        if player_score > 21:
            print("You busted! Dealer wins.")
        elif dealer_score > 21:
            print("Dealer busted! You win!")
        elif player_score > dealer_score:
            print("You win!")
        elif dealer_score > player_score:
            print("Dealer wins!")
        else:
            print("It's a draw!")

    play_again = input("Do you want to play again? 'y' or 'n' ").lower()
    if play_again == 'y':
        player_busted = False
        player_hand.clear()
        dealer_hand.clear()
        play_blackjack()
    else:
        print("Good Bye")

buy_in = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if buy_in == 'y':
    play_blackjack()
else:
    print("Good Bye")