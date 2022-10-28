# 생각할 부분
# 1. 각 위젯에 대한 변수명 어떻게 지을지
# 2. string 으로 변경할 때 fstring 사용. ex) f"{km}"
# 3. component 의 속성 값을 변경하려면 dictionary 사용하듯이 해야함(실제로 dictionary 인듯).
# ex) label_miles["text"] = f"{km}" 이런식으로 해줘야 함.

from tkinter import *

MILE_TO_KILOMETER_RATIO = 1.609344

window = Tk()
window.title("miles to kilometer converter")
window.config(padx=50, pady=20)
window.minsize(width=330, height=50)

mile_entry = Entry(width=20)
mile_entry.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_before_kilometer = Label(text="is equal to")
label_before_kilometer.grid(column=0, row=1)

label_kilometer = Label(text="0")
label_kilometer.grid(column=1, row=1)

label_after_kilometer = Label(text="Km")
label_after_kilometer.grid(column=2, row=1)


def mile_to_kilometer():
    miles = int(mile_entry.get())
    #label_kilometer["text"] = str(miles * MILE_TO_KILOMETER_RATIO)
    km = round(miles * MILE_TO_KILOMETER_RATIO, 2)
    label_kilometer["text"] = f"{km}"


button_calculation = Button(width=10, height=1, command=mile_to_kilometer, text="Calculate")
button_calculation.grid(row=2, column=1)
window.mainloop()