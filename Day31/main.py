import tkinter
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"


window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_front = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="French", font=("Arial", 20))
word = canvas.create_text(400, 250, text="Apple", font=("Arial", 30))
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=1)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image)
#wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.config(bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

#right_button = tkinter.Button(width=10, image="images/right.png")
right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image)
right_button.config(bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=2)


window.mainloop()