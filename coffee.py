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
def is_resource_enough(ingredients):
    for item in ingredients:
        if resources[item] < drink["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
        elif resources[item] >= drink["ingredients"][item]:
            process_coins()
            return True
def process_coins():
    sum = 0.25 * quarters
    sum += 0.1 * dimes
    sum += 0.05 * nickles
    sum += 0.25 * pennies
    sum = round(sum, 2)
    return sum
def transaction_successful(sum, cost):
    if sum < cost:
        print(f"Sorry that's not enough money. Money{sum} refunded.")
        return False
    elif sum >= cost:
        change = round(sum - cost, 2)
        if change != 0:
            print(f"paid coins are more than enough. ${change} refunded")
        global profit
        profit += cost
        return True

def make_coffee(choice_drink,ingredients):
    """returns the ingredients remaining from the report"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice_drink}. Enjoy!!")
profit = 0
should_repeat = True
while should_repeat:
    choice_drink = input("What coffee would you like to have? 'Espresso', 'Latte' or 'Cappuccino' ")
    if choice_drink == "off":
        print("Turning off machine...🎰")
        should_repeat = False
    elif choice_drink == "report":
        print(f"Water:{resources['water']}ml.")
        print(f"Milk:{resources['milk']}ml.")
        print(f"Coffee:{resources['coffee']}g.")
        print(f"Money: ${profit}")
    else:
        #making drink
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        drink = MENU[choice_drink]
        if is_resource_enough(drink["ingredients"]):
            sum = process_coins()
            print(f"Inserted coins is in sum of ${sum}.")
            if transaction_successful(sum, drink["cost"]):
                make_coffee(choice_drink,drink["ingredients"])
                resources["cost"] = profit

