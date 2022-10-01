#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# ver 1
'''
password = ''
symbol_list = [letters, symbols, numbers]
size_list = [nr_letters, nr_symbols, nr_numbers]

total_size = nr_letters + nr_symbols + nr_numbers

for i in range(0, total_size):
    kind = random.randint(0, len(size_list) - 1)
    #random_index = random.randint(0, len(symbol_list[kind]) - 1)
    #password += symbol_list[kind][random_index]

    password += random.choice(symbol_list[kind])
    size_list[kind] -= 1
    if size_list[kind] == 0:
        #symbol_list.remove()
        symbol_list.pop(kind)
        size_list.pop(kind)
'''

#ver2
#'''
password_list = []
for c in range(nr_numbers):
    password_list.append(random.choice(numbers))
for c in range(0, nr_letters):
    password_list.append(random.choice(letters))
for c in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

#password = "".join(str(x) for x in password_list)
password = ""
for c in password_list:
    password += c
#'''
print(password)