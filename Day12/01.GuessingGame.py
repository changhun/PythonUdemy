import random
from art import logo


def guess_game():
    print(logo)
    print("Welcome to Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        life = 10
    elif difficulty == 'hard':
        life = 5

    answer = random.randint(1, 100)
    guess = -1

    while life > 0 and guess != answer:
        print(f"You have {life} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))
        if guess == answer:
            print("Success!!")
        else:
            if guess > answer:
                print("Too high.")
            else:
                print("Too low.")
            life -= 1
            if life > 0:
                print("Guess again.")

guess_game()

