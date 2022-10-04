import random


def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def play_game():
    my_cards = []
    dealer_cards = []
    my_cards.append(get_card())
    dealer_cards.append(get_card())

    should_continue = 'y'
    while should_continue == 'y':
        my_cards.append(get_card())
        dealer_cards.append(get_card())

        #print(f"Your cards: {my_cards}, current score: {my_cards.sum()}")
        print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if sum(my_cards) > 21:
            should_continue = 'n'
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if sum(dealer_cards) <= 16:
        dealer_cards.append(get_card())

    print(f"Your final hand: {my_cards}. Your final score: {sum(my_cards)}")
    print(f"Computer's final hand: {dealer_cards}. Computer's final score:{sum(dealer_cards)}")
    if sum(my_cards) > 21:
        print("You went over. You lose.")
    elif sum(dealer_cards) > 21:
        print("Opponent went over. You win.")
    else:
        if sum(my_cards) > sum(dealer_cards):
            print("You win.")
        elif sum(my_cards) < sum(dealer_cards):
            print("You lose.")
        else:
            print("Draw.")


continue_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
while continue_game == 'y':
    play_game()
    continue_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

