import tkinter
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------------------- Data load --------------------------------- #
data = pandas.read_csv("data/french_words.csv")
words_dict = data.to_dict(orient="record")

# -------------------------------- Functions --------------------------------- #
rand_word = {}
is_front = False


def next_card():
    global is_front
    if is_front:
        return
    global rand_word
    rand_word = random.choice(words_dict)
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=rand_word["French"])
    canvas.itemconfig(canvas_image, image=card_front_image)
    window.after(3000, flip_card)
    is_front = True


def flip_card():
    global rand_word
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=rand_word["English"])
    canvas.itemconfig(canvas_image, image=card_back_image)

    global is_front
    is_front = False

# -------------------------------- UI --------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)

language = canvas.create_text(400, 150, text="French", font=("Arial", 20))
word = canvas.create_text(400, 250, text="Apple", font=("Arial", 30))
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

is_front = False
next_card()

window.mainloop()
