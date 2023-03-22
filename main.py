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
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def process_coins():
    print('Please insert coins.')
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def check_payment(payment, cost):
    print('checking payment...')
    if payment >= cost:
        print("making your drink...")
        change = payment - cost
        global money
        money += cost
        print(f"Your change is ${change}")
        print(f"coffee machine cash on hand: {money}")
        return True
    else:
        print("Insufficient funds. Money refunded.")
        return False



while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): ")

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}ml")
        print(f"Money ${money}")
    else:
        drink = MENU[choice]
        order_ingredients = drink['ingredients']
        if check_resources(order_ingredients):
            print('making your drink')
            payment = process_coins()
            print(f"total received: {payment}")
            check_payment(payment, drink['cost'])
        else:
            is_on = False
