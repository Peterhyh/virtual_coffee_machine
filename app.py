

water = 300
milk = 200
coffee = 100
money = 0

while True:
    user_selection = input(
        'What would you like? (espresso/latte/cappuccino): ')

    if user_selection == 'report':
        format_money = "{:.2f}".format(money)
        print(
            f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${format_money}')
    elif user_selection == 'espresso':
        cost = 2.5
        print('Please insert coins.')
        quarters = input('How many quarters?: ')
        dimes = input('How many dimes?: ')
        nickels = input('How many nickels?: ')
        pennies = input('How many pennies?: ')
    elif user_selection == 'latte':

        while True:
            print('Please insert coins.')
            quarters = float(input('How many quarters?: ')) * 0.25
            dimes = float(input('How many dimes?: ')) * 0.10
            nickels = float(input('How many nickels?: ')) * 0.05
            pennies = float(input('How many pennies?: ')) * 0.01

            change = (quarters + dimes + nickels + pennies) - cost
            format_change = '{:.2f}'.format(change)
            if change < 0:
                print('You do not have enough money.')
            elif change > 0:
                print(f'Your change is ${format_change}')
                break
            else:
                break
            water -= 200
            milk -= 150
            coffee -= 24
            money += cost
            cost = 2.50
        print('Here is your latte ☕ Enjoy!')

    elif user_selection == 'cappuccino':
        cost = 2.5
        print('Please insert coins.')
        quarters = input('How many quarters?: ')
        dimes = input('How many dimes?: ')
        nickels = input('How many nickels?: ')
        pennies = input('How many pennies?: ')
