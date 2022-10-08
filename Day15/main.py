from menu import MENU


# TODO: 2. define report function
def report(current_resources):
    print(f"water: {current_resources['water']}")
    print(f"milk: {current_resources['milk']}")
    print(f"coffee: {current_resources['coffee']}")
    print(f"money: {current_resources['money']}")


# TODO: 3. define function of checking resource
def check_resource_enough(cur_resources, ingredients):
    for ingredient in ingredients:
        if cur_resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry, There is not enough {ingredient}.")
            return False
    return True


def deduct_ingredients(cur_resources, ingredients):
    for ingredient in ingredients:
        #print(f"{ingredient}. current: {cur_resources[ingredient]}, menu: {ingredients[ingredient]}")
        cur_resources[ingredient] -= ingredients[ingredient]
        #print(f'After deducted: {cur_resources[ingredient]}\n')


# TODO: 4. define function of processing coin
def process_coin(cost):
    print(f'Please insert coin. cost: {cost}')
    quarter_count = int(input("How many quarters?: "))
    dime_count = int(input("How many dimes?: "))
    nickle_count = int(input("How many nickles?: "))
    penny_count = int(input("How many pennies?: "))
    total = quarter_count * 0.25 + dime_count * 0.1 + nickle_count * 0.05 + penny_count * 0.01
    return total


# resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
# 그냥 int 형 변수가 아닌 자료형으로 만들면 함수의 인자로 넣어서 변경할 수 있다!!!

"""
water = 300
milk = 200
coffee = 100
money = 0
"""
coins = 0


turned_on = True

while turned_on:
    # TODO: 1. print prompt
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        turned_on = False
    elif choice == "report":
        report(resources)
    #elif is_menu(choice):
    elif choice in MENU:
        if not check_resource_enough(resources, MENU[choice]["ingredients"]):
            continue

        coins += process_coin(MENU[choice]["cost"])
        if coins < MENU[choice]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
            continue

        resources["money"] += MENU[choice]["cost"]
        coins -= MENU[choice]["cost"]

        if coins > 0:
            print(f"Here is ${round(coins, 2)} dollars in change.")
            coins = 0

        deduct_ingredients(resources, MENU[choice]["ingredients"])
        print(f'Here is your {choice}. Enjoy!!')




    #