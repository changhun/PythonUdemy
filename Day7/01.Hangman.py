#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"choosen word is {chosen_word}")


#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in chosen_word:
    display += '_'

end_of_game = False
while not end_of_game:
    print(display)
    choice = input("Guess a letter: ").lower()

    hit = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == choice:
            hit = True
            display[i] = choice

    if not hit:
        lives -= 1
    hit = False

    if lives == 0:
        print("Game Over")
        print(stages[lives])
        break

    if display.count('_') == 0:
        end_of_game = True
        print("You win!!")

    print(stages[lives])
