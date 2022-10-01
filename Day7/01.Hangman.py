#Step 4

import random

# import hangman_art
# import hangman_words
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#print(f"choosen word is {chosen_word}")


#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in chosen_word:
    display += '_'

#from replit import clear
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(''.join(display))

    #clear()
    if guess in display:
        print("You've already guessed it")

    else:
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, but that's not in the word. You lose a life")
            if lives == 0:
                print("Game Over")
                print(stages[lives])
                break
        else:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess

    if '_' not in display:
        end_of_game = True
        print("You win!!")

    print(stages[lives])
