import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class GraphicUserInterface:
    def __init__(self, game_brain: QuizBrain):
        self.quiz = game_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #self.label = tkinter.Label(text="score: 0", fg="white", bg=THEME_COLOR, pady=30)
        self.label = tkinter.Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 120)
        self.canvas.itemconfig(self.question_text, width=300, font=("Arial", 15, "italic"), fill=THEME_COLOR)

        check_image = tkinter.PhotoImage(file="images/true.png")
        self.check_button = tkinter.Button(image=check_image, highlightthickness=0, command=self.check_button_clicked)
        self.check_button.grid(row=3, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.false_button_clicked)
        self.false_button.grid(row=3, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if not self.quiz.still_has_questions():
            print("Out of questions. Getting more questions from web.")
            self.quiz.get_questions_from_web()
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        #self.canvas.config(bg="WHITE")
        self.canvas["bg"] = "WHITE"

    def check_button_clicked(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def false_button_clicked(self):
        result = self.quiz.check_answer("False")
        self.get_feedback(result)

    def get_feedback(self, result: bool):
        if result is False:
            self.canvas["bg"] = "RED"
        else:
            self.canvas.config(bg="GREEN")
        self.label["text"] = f"score: {self.quiz.get_score()}"
        self.window.after(100, self.next_question)
