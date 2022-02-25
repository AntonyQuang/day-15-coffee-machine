def coffee_choice(MENU):
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee in MENU or coffee == "off" or coffee == "report":
        return coffee
    else:
        coffee_choice(MENU)


def print_report(resources, total):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    cost = total
    print(f"Water : {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${total}")


def resource_check(MENU, coffee, resources):
    ingredients = MENU[coffee]["ingredients"]
    component = ("water", "milk", "coffee")
    check = True
    for item in component:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}")
            check = False
    return check


def coin_processor():
    coin_value = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    print("Please insert coins")
    coins_inserted = {
        "quarters": 0,
        "dimes": 0,
        "nickels": 0,
        "pennies": 0,
    }
    for k in coins_inserted:
        coins_inserted[k] = int(input(f"How many {k}?: "))

    money = 0
    for k in coin_value:
        money += coin_value[k] * coins_inserted[k]

    return money


def make_coffee(coffee, MENU, resources):
    coffee_resource = MENU[coffee]["ingredients"]
    for item in coffee_resource:
        resources[item] -= coffee_resource[item]
    print(f"Here is your {coffee}. ☕ Enjoy!")
    return resources


def coffee_machine():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk": 0,
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

    power = True
    total = 0
    while power:
        coffee = coffee_choice(MENU)
        if coffee == "report":
            print_report(resources, total)
        elif coffee == "off":
            power = False
        else:
            resource = resource_check(MENU, coffee, resources)
            if resource:
                payment = coin_processor()
                cost = MENU[coffee]["cost"]
                if payment > cost:
                    print(f"Here is ${round(payment - cost,2)} in change.")
                if payment >= cost:
                    resources = make_coffee(coffee, MENU, resources)
                    total += MENU[coffee]["cost"]
                else:
                    print("Sorry that is not enough money. Money refunded.")


coffee_machine()
