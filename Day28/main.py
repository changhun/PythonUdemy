# 생각해볼 것
# 시간되면 pop up 하도록
# pixel, png, jpg
# png 파일 크기 200 * 203 의미가 뭔지
# canvas 는 padx, pady 없나?

import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#182747"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #timer_label.text = "Timer" # 이렇게 하면 적용 안 됨
    timer_label["text"] = "Timer"
    canvas.itemconfig(timer_text, text="00:00")
    #checkmark.text = ""
    checkmark["text"] = ""
    global rep
    rep = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep

    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    # short_break_sec = 1
    # long_break_sec = 1
    # work_sec = 2
    count = 0
    if rep % 8 == 0:
        count = long_break_sec
        timer_label.config(text="L-Break", fg=BLUE)
    elif rep % 2 == 0:
        count = short_break_sec
        timer_label.config(text="S-Break", fg=RED)
    else:
        count = work_sec
        timer_label.config(text="Work", fg=GREEN)

    rep += 1
    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(count/60)
    count_sec = str(count % 60)

    #canvas.itemconfig(timer_text, text=count)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec.zfill(2)}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        num_work_completed = rep//2
        checkmark["text"] = "✔" * num_work_completed
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("POMODORO")
#window.configure(padx=100, pady=50)
window.config(padx=100, pady=50, bg=PINK)

timer_label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg = PINK)
#timer_label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg = PINK)
timer_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, highlightthickness=0)
canvas.config(bg=PINK)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
# canvas의 text 도 변수로 가리킬 수 있나봄.
timer_text = canvas.create_text(102, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
#count_down(5)

# canvas 에 button 은 추가하지 못하나?
#button_canvas = tkinter.Canvas(width=200, height=10)


start_button = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

#checkmark = tkinter.Label(text="✔", fg=GREEN, bg=PINK, font=(FONT_NAME, 20, "bold"))
checkmark = tkinter.Label(fg=GREEN, bg=PINK, font=(FONT_NAME, 20, "bold"))
checkmark.grid(row=3, column=1)

reset_button = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

window.mainloop()
