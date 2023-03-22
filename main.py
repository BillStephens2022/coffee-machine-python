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
}

# TODO: 1.  Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# TODO: 2.  Turn off the coffee machine by entering "off" to the prompt.
# TODO: 3.  Print report of resources.
# TODO: 4.  Check resources sufficient?
# TODO: 5.  Process coins.
# TODO: 6.  Check transactions successful?
# TODO: 7.  Make coffee.

is_on = True
money = 0

def check_resources(order_ingredients):
    """checks if there is enough resources in the coffee machine to make the drink"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def process_coins():
    """prompts user to inssert coins and returns total dollar amount received"""
    print('Please insert coins.')
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def check_payment(payment, cost):
    """checks if payment is sufficient"""
    if payment >= cost:
        change = payment - cost
        global money
        money += cost
        print(f"Your change is ${round(change, 2)}\n")
        return True
    else:
        print("Insufficient funds. Money refunded.")
        return False
    
def make_coffee(drink, order_ingredients):
    """deducts resources used to make the drink"""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink} ☕️. Enjoy!!\n\n\n")


print(logo)
while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): ")

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print("\n\nCoffee Machine Resource Report:\n")
        print(f"Water {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}ml")
        print(f"Money ${money}\n\n")
    else:
        drink = MENU[choice]
        order_ingredients = drink['ingredients']
        if check_resources(order_ingredients):
            print(f"\nThe price for a {choice} is ${drink['cost']}.")
            payment = process_coins()
            print(f"\nTotal received: ${round(payment, 2)}\n")
            if check_payment(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
        else:
            is_on = False
