entry = {}


def add_bid():
    bidder = input("What is your name?: ")

    # Convert the bid to a float or int
    bid = float(input("What is your bid?: $"))

    # Store the bid in the dictionary
    entry[bidder] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidders == 'yes':
        print("\n" * 30)
        add_bid()
    else:
        check_bids(entry)


def check_bids(bid_dic):
    highest_bid = 0
    winner = None

    for bidder, bid_amount in bid_dic.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\nThe winner is {winner} with a bid of ${highest_bid:.2f}")


# Start the bidding process
add_bid()
