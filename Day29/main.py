import tkinter
from tkinter import messagebox
import random
import pyperclip

WIDTH=45


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
        with open("password_file.txt", "a") as password_file:
            password_file.write(f"{website} | {username} | {password}\n")
        website_entry.delete(0, "end")
        password_entry.delete(0, "end")


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
website_entry = tkinter.Entry(width=WIDTH)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = tkinter.Entry(width=WIDTH)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "changhun611")

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=28)
password_entry.grid(row=3, column=1)
password_button = tkinter.Button(text="GeneratePassword", font=("Arerial, 8"), command=create_password)
password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=WIDTH, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()