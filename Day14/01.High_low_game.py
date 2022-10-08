import game_data
import random
import art


def compare_item(item1, item2):
    if item1['follower_count'] >= item2['follower_count']:
        return True
    else:
        return False


first_item = random.choice(game_data.data)
second_item = random.choice(game_data.data)
print(f"Compare A: {first_item['name']}, {first_item['description']}, {first_item['country']}")
print(art.vs)
print(f"Compare B: {second_item['name']}, {second_item['description']}, {second_item['country']}")

score = 0
should_continue = True
while should_continue:
    #repl.clear()
    print(art.logo)
    if score > 0:
        print(f"You are right. Current score: {score}")
    print(f"Compare A: {first_item['name']}, {first_item['description']}, {first_item['country']}")
    print(art.vs)
    print(f"Compare B: {second_item['name']}, {second_item['description']}, {second_item['country']}")
    choice = input("Who has more followers? Type A or B: ").lower()

    if choice == 'a' and compare_item(first_item, second_item):
        score += 1
    elif choice == 'b' and compare_item(second_item, first_item):
        score += 1
        first_item = second_item
    else:
        should_continue = False
        print(f"Sorry. That's wrong. Your score is {score}")

    if should_continue:
        second_item = random.choice(game_data.data)

