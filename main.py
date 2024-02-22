from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


# prints a report of all coffee machine resources
def report():
    for key, value in resources.items():
        print(key, ":", value)


# Checks resources are sufficient to make drink order.
def check_resources(water_amount, milk_amount, coffee_amount):
    if resources["water"] < water_amount:
        print("Sorry there is not enough water.")
        return False

    if resources["milk"] < milk_amount:
        print("Sorry there is not enough milk.")
        return False

    if resources["coffee"] < coffee_amount:
        print("Sorry there is not enough coffee.")
        return False

    return True


# Asks the user for how many of each coin they would like to use
# formats them to the correct decimals and adds them together
def insert_coins():
    twenty_pence = int(input("How many 20p coins do you want to insert?:")) * 20
    fifty_pence = int(input("How many 50p coins do you want to insert?:")) * 50
    pound_coins = int(input("How many pound coins do you want to insert?"))
    total_coins = (twenty_pence * 0.01) + (fifty_pence * 0.01) + pound_coins
    return total_coins

# Deducts the resources depending on the drink chosen and resources needed to make that drink
def deduct_resources(water_amount, milk_amount, coffee_amount):
    resources['milk'] -= milk_amount
    resources['water'] -= water_amount
    resources['coffee'] -= coffee_amount

# main function
def coffee_machine():
    off = False
    enough_resources = True

    while not off and enough_resources:
        print(logo)
        users_choice = input("What would you like? (espresso/latte/cappuccino):")

        if users_choice == "off":
            off = True

        elif users_choice == "report":
            report()

        elif users_choice == "latte":
            water_resources = (MENU['latte']['ingredients']['water'])
            milk_resources = (MENU['latte']['ingredients']['milk'])
            coffee_resources = (MENU['latte']['ingredients']['coffee'])
            enough_resources = check_resources(water_resources, milk_resources, coffee_resources)

            if not enough_resources:
                off = True

            elif enough_resources:
                print(f"That will be £{MENU['latte']['cost']:.2f}")
                coins = insert_coins()

                if coins < (MENU['latte']['cost']):
                    print("Sorry, you don't have enough, money refunded")

                elif coins >= (MENU['latte']['cost']):
                    resources['money'] += coins
                    deduct_resources(water_resources, milk_resources, coffee_resources)

                    if coins > MENU['latte']['cost']:
                        change = coins - MENU['latte']['cost']
                        print(f"Here is £{change:.2f} in change")
                        print("Here is your latte, enjoy!")

        elif users_choice >= "espresso":
            water_resources = (MENU['espresso']['ingredients']['water'])
            coffee_resources = (MENU['espresso']['ingredients']['coffee'])
            enough_resources = check_resources(water_resources, 0, coffee_resources)

            if not enough_resources:
                off = True

            elif enough_resources:
                print(f"That will be £{MENU['espresso']['cost']:.2f}")
                coins = insert_coins()

                if coins < (MENU['espresso']['cost']):
                    print("Sorry, you don't have enough, money refunded")

                elif coins >= (MENU['espresso']['cost']):
                    resources['money'] += coins
                    deduct_resources(water_resources, 0, coffee_resources)
                    if coins > MENU['espresso']['cost']:
                        change = coins - MENU['espresso']['cost']
                        print(f"Here is £{change:.2f} in change")
                        print("Here is your espresso, enjoy!")

        elif users_choice == "cappuccino":
            water_resources = (MENU['cappuccino']['ingredients']['water'])
            milk_resources = (MENU['cappuccino']['ingredients']['milk'])
            coffee_resources = (MENU['cappuccino']['ingredients']['coffee'])
            enough_resources = check_resources(water_resources, milk_resources, coffee_resources)

            if not enough_resources:
                off = True

            elif enough_resources:
                print(f"That will be £{MENU['cappuccino']['cost']:.2f}")
                coins = insert_coins()

                if coins < (MENU['cappuccino']['cost']):
                    print("Sorry, you don't have enough, money refunded")

                elif coins >= (MENU['cappuccino']['cost']):
                    resources['money'] += MENU['cappuccino']['cost']
                    deduct_resources(water_resources, milk_resources, coffee_resources)

                    if coins > MENU['cappuccino']['cost']:
                        change = coins - MENU['cappuccino']['cost']
                        print(f"Here is £{change:.2f} in change")
                        print("Here is your cappuccino, enjoy!")


coffee_machine()