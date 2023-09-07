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
    "cappuccino":{
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}


resources = {'water': 300, 'milk': 200, 'coffee': 100}
money = 0
is_on = True

def check_resource(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f'Sorry, there is not enough {ingredient}.')
            return False
    return True


def process_coins():
    print('Please insert coins.')
    total = float(input('How many quarters?: ')) * 0.25
    total += float(input('How many dimes?: ')) * 0.10
    total += float(input('How many nickels?: ')) * 0.05
    total += float(input('How many pennies?: ')) * 0.01
    return total

def check_transaction(user_payment, drink_cost):
    if user_payment > drink_cost:
        change = user_payment - drink_cost
        format_change = '{:.2f}'.format(change)
        print(f'Your change is ${format_change}')
        return True
    elif user_payment < drink_cost:
        print(f'You did not insert enough money.')
        return False
    else:
        return True
    
def subtract_ingredients(used_ingredients, inventory):
    for item in inventory:
        remaining = inventory[item] - used_ingredients[item]
        inventory[item] = remaining
    

while is_on:
    user_selection = input(
        'What would you like? (espresso/latte/cappuccino): ')
    if user_selection == 'off':
        is_on = False
    elif user_selection == 'report':
        format_money = "{:.2f}".format(money)
        print(
            f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${format_money}')
    else:
        drink = MENU[user_selection]
        if check_resource(drink['ingredients']):
            payment = process_coins()
            if check_transaction(payment, drink['cost']):
                subtract_ingredients(drink['ingredients'], resources)
                print(f'Here is your {user_selection} ☕ Enjoy!')

                

