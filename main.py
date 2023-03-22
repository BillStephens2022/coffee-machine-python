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

# TODO: 1.  Prompt user by asking "What would you like? (espresso/latte/capuccino):"
# TODO: 2.  Turn off the coffee machine by entering "off" to the prompt.
# TODO: 3.  Print report of resources.
# TODO: 4.  Check resources sufficient?
# TODO: 5.  Process coins.
# TODO: 6.  Check transactions successful?
# TODO: 7.  Make coffee.

is_on = True

choice = input("What would you like? (espresso, latte, capuccino): ")
