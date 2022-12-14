import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

WIDTH=48


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def create_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, "end")
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    print(website)

    # if website is None:
    #if website == "" or username == "" or password =="":
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        print("website is empty")
        messagebox.showwarning(title="Oops", message="Please make sure you haven't any field empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\n user: {username}"
                                   f"\npassword: {password}\n Is it ok to save?")
    if is_ok:
        new_data = {
            website: {
                "user" : username,
                "password": password
            }
        }

        try:
            with open("data.json", "r") as json_file:
                json_data = json.load(json_file)
        except FileNotFoundError:
            with open("data.json", "w") as json_file:
                json.dump(new_data, json_file, indent=4)
        else:
            with open("data.json", "w") as json_file:
                json_data.update(new_data)
                json.dump(json_data, json_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ----------------------- Search Password ----------------------------- #
def search_password():
    try:
        with open("data.json", "r") as json_file:
            json_data = json.load(json_file)
            website = website_entry.get()
            if len(website) == 0:
                messagebox.showwarnning(title="Oops", message="Sorry 'website' field is empty.")
                print("Sorry 'website' field is empty.")
                return
            username = json_data[website]["user"]
            password = json_data[website]["password"]
    except FileNotFoundError:
        messagebox.showwarning(title="Data File not Found",
                               message=f"Sorry there's no information in {website}.")
        print(f"Sorry there's no information in {website}.")
    except KeyError:
        messagebox.showwarning(title="Website not Found",
                               message=f"Sorry there's no information in {website}.")
        print(f"Sorry there's no information in {website}.")
    else:
        messagebox.showinfo(title=website, message=f"user: {username}\npassword: {password}")
    finally:
        website_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
#window = tkinter.Tk(width=240, height=240, title="Password manager")
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, width=240, height=240)

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = tkinter.Entry(width=30)
website_entry.focus()
# website_entry.grid(row=1, column=1, columnspan=2)
website_entry.grid(row=1, column=1)
website_search_button = tkinter.Button(text="Search", width=16, command=search_password)
website_search_button.grid(row=1, column=2)

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = tkinter.Entry(width=WIDTH)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "changhun611")

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=30)
password_entry.grid(row=3, column=1)
password_button = tkinter.Button(text="GeneratePassword", font=("Arerial, 8"), command=create_password)
password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=WIDTH, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()