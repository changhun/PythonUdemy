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


text = tkinter.Text(height=5, width=30)
text.focus()
text.insert(tkinter.END, "Example of multi-line entry.")
print(text.get("1.0", tkinter.END))
text.pack()


def spinbox_used():
    print(spinBox.get())


# from_ 인자는 왜 _ 가 붙지?
spinBox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinBox.pack()


def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=10, width=5, command=scale_used)
scale.pack()


def check_button_used():
    print(check_state.get())


check_state = tkinter.IntVar()
check_button = tkinter.Checkbutton(text="Is On?", variable=check_state, command=check_button_used)
check_button.pack()


def radio_button_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()
radio_button = tkinter.Radiobutton(text="Opinion1", value=1, variable=radio_state, command=radio_button_used)
radio_button.pack()
radio_button2 = tkinter.Radiobutton(text="Opinion2", value=2, variable=radio_state, command=radio_button_used)
radio_button2.pack()


def list_box_used(event):
    print(listBox.get(listBox.curselection()))


listBox = tkinter.Listbox(height=4)
Fruits = ["apple", "banana", "orange", "pineapple"]
for fruit in Fruits:
    listBox.insert(Fruits.index(fruit), fruit)
listBox.bind("<<ListboxSelect>>", list_box_used)
listBox.pack()

window.mainloop()
