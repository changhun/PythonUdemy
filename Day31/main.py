import tkinter
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------------------- Data load --------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    if len(data) == 0:
        data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    words_dict = data.to_dict(orient="record")
    #print(words_dict)

# -------------------------------- Functions --------------------------------- #
rand_word = {}


def next_card():
    global rand_word, flip_time
    window.after_cancel(flip_time)
    rand_word = random.choice(words_dict)
    canvas.itemconfig(language, text="French", fill="Black")
    canvas.itemconfig(word, text=rand_word["French"], fill="Black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_time = window.after(3000, flip_card)


def flip_card():
    global rand_word
    canvas.itemconfig(language, text="English", fill="White")
    canvas.itemconfig(word, text=rand_word["English"], fill="White")
    canvas.itemconfig(canvas_image, image=card_back_image)


def remove_card():
    global rand_word
    words_dict.remove(rand_word)
    #print(len(words_dict))
    next_card()
    words_dataframe = pandas.DataFrame(words_dict)
    # dataframe 을 csv 로 저장할 때 index 는 생성하지 않도록 한다.
    words_dataframe.to_csv("data/words_to_learn.csv", index=False)


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
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

#next_card()
flip_time = window.after(0, next_card)

window.mainloop()
