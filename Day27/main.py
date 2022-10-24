import tkinter


window = tkinter.Tk()
window.title("My first GUI window")
window.minsize(500, 300)

my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label.pack()


input = tkinter.Entry(width=10)
input.pack()


def button_click_event():
    print("I got clicked")
    #my_label["text"] = "Button got clicked"
    my_label["text"] = input.get()


button = tkinter.Button(text="Click Me", command=button_click_event)
button.pack()





window.mainloop()
