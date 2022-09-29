
"""
print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm?"))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?"))
    if age < 12:
        print("Please pay 5$")
    elif age <= 18:
        print("Please pay 7$")
    else:
        print("Please pay 12$")
else:
    print("Sorry, you have to grow taller before you can ride")
"""


# 2 even or odd

# number = int(input("Which number do you want to check?"))
#
# if number%2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

"""
height = float(input("Input your height: "))
weight = float(input("Input your weight: "))

bmi = round(weight / height**2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You are normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, You are Overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, You are Obese")
else:
    print(f"Your bmi is {bmi}, You are clinically obese")
"""

# Leap Year
"""
year = int(input("Input Year: "))

if year % 400 == 0:
    print("Leap")
elif year % 100 == 0:
    print("Not Leap")
elif year % 4 == 0:
    print("Leap")
else:
    print("Not Leap")
"""

#Pizza Order
"""
print("Welcome to python pizza delivers")
pizza_size = input("What size pizza do you want? S, M, L")
add_pepperoni = input("Do you want additional pepperoni? Y or N")
add_cheese = input("Do you want additional cheese? Y or N")


if pizza_size == 'S':
    price = 15
elif pizza_size == 'M':
    price = 20
else:
    price = 25

if add_pepperoni:
    if pizza_size == 'S':
        price += 2
    else:
        price += 3

if add_cheese:
    price += 1

print(f"Your final bill is {price}")
"""

# Love Calculator
"""
name1 = input("Input name1: ")
name2 = input("Input name2: ")

count_true = name1.lower().count('t')
count_true += name1.lower().count('r')
count_true += name1.lower().count('u')
count_true += name1.lower().count('e')

count_true += name2.lower().count('t')
count_true += name2.lower().count('r')
count_true += name2.lower().count('u')
count_true += name2.lower().count('e')

count_love = name1.lower().count('l')
count_love += name1.lower().count('o')
count_love += name1.lower().count('v')
count_love += name1.lower().count('e')
count_love += name2.lower().count('l')
count_love += name2.lower().count('o')
count_love += name2.lower().count('v')
count_love += name2.lower().count('e')

result = count_true * 10 + count_love

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
#elif 40 <= result and result <= 50:
elif 40 <= result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
"""


#Game
print('''
                   _..
  /}_{\           /.-'
 ( a a )-.___...-'/
 ==._.==         ;
      \ i _..._ /,
      {_;/   {_//  fsc
''')
print("Welcome to treasure Island.")
direction = input("left or right? \n").lower()
if direction == "right":
    print("Game Over.")
else:
    transport = input("Wait or Swim? \n").lower()
    if (transport == "swim"):
        print("Game Over")
    else:
        room = input("Choose room. Red or Blue or Yellow\n").lower()
        if room == "yellow":
            print("You found tremendous treasure!!! You don't have to go to work")
        else:
            print("Fire!!! Game Over.")
