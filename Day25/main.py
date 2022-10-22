import turtle as t
import pandas


FONT = ('Arial', 8, 'normal')

screen = t.Screen()
image = "blank_states_img.gif"
screen.addshape(image)

turtle = t.Turtle()
turtle.shape(image)

score = 0
num_states = 50

df = pandas.read_csv("50_states.csv")
state_list = df.state.tolist()

state_text = t.Turtle()
t.hideturtle()
t.penup()

end_of_game = False
while not end_of_game:
    answer_temp = screen.textinput(title=f"Correct {score}/{num_states}", prompt="What's another state's name?")
    # End game when cancel is clicked()
    if answer_temp is None:
        end_of_game = True

    answer = answer_temp.title()
    row = df[df["state"] == answer]
    #if len(row) != 0:
    if answer in state_list:
        state_list.remove(answer)
        score += 1
        # xcor = row["x"].tolist()[0]
        # ycor = row["y"].tolist()[0]
        # t.goto(xcor, ycor)

        # row.x 는 series type 인데 어떻게 int 를 하면 첫번째 요소의 값을 int 로 하여 사용되는 거지?
        print(type(int(row.x)))
        t.goto(int(row["x"]), int(row["y"]))

        t.write(row.state.item(), align="left", font=FONT)


t.mainloop()

#screen.exitonclick()