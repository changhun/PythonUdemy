import random

#random
'''
random_integer = random.randint(100, 200)
print(random_integer)

random_number = random.random()
print(random_number*5)
'''

#Heads or Tails
'''
random_int = random.randint(0,1)
if random_int == 0:
    print("Heads")
else:
    print("Tails")
'''


# List
'''
names = input("Give me everybody's name separated with comma\n")

name_list = names.split(", ")
#print(name_list)
#size = name_list.len()
size = len(name_list)
rand = random.randint(0, size-1)
print(f"{name_list[rand]} will pay the bill")
'''

# Treasure
'''
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# pos_int = int(position)
# col = int(pos_int / 10)
# row = pos_int % 10
col = int(position[0])
row = int(position[1])

#print(f"col={col}, row = {row}")
map[row-1][col-1] = 'X '
print(f"{row1}\n{row2}\n{row3}")
'''

# Rock Paper scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = int(input("What do you want to choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors\n"))
computer_choice = random.randint(0, 2)
pic = [rock, paper, scissors]

print(f"Your choice\n{pic[your_choice]}\n")
print(f"Computer's choice\n{pic[computer_choice]}")

if your_choice - computer_choice == 1 or your_choice - computer_choice == -2:
    print("You win!!")
elif your_choice == computer_choice:
    print("Same")
else:
    print("You lose")