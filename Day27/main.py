import tkinter


window = tkinter.Tk()
window.title("My first GUI window")
window.minsize(500, 300)

my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()

