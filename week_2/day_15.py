resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0

}

menu = {
    "espresso": {
        "recipe": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.5,

    },
    "latte": {
        "recipe": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 2.5,
    },
    "cappuccino": {
        "recipe": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "price": 3.0,
    }
}

ordering = True

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

# TODO: print report
def report():
    print(f"The coffee machines current resources are:")
    for item in resources:
        print(f"{item}: {resources[item]}")

def check_resources(order_ing):
    for item in order_ing:
        if order_ing[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def coins():
    """Returns total money given"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total




is_on = True
while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino):\n").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    else:
        drink = menu[choice]
        if check_resources(drink["recipe"]):
            print(f"{choice} costs ${drink["price"]}")
            payment = coins()
            if payment >= drink["price"]:
                change = (float(payment) - float(drink["price"])).__round__(2)
                print(f"Your change is ${change}")
                resources["money"] += drink["price"]
                for item in drink["recipe"]:
                    resources[item] -= drink["recipe"][item]
                print(f"\nHere is your {choice}. Enjoy! ☕")
            else:
                print("Sorry that's not enough money. Money refunded.")
                print("Please try again")



        # print(drink)


# def check_resource():
#     if choice

print("\nTurning off...")
print("Good bye.")