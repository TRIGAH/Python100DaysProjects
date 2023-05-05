from turtle import Screen,Turtle
import pandas
import time
screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
screen.addshape("us-states-game\\blank_states_img.gif")
turtle.shape("us-states-game\\blank_states_img.gif")

game_is_on = True
correct_state_count = 0
correct_states_guess = []
us_states_data = pandas.read_csv("us-states-game\\50_states.csv")
states=us_states_data.state.to_list()
while len(correct_states_guess) < 50:
    state_guess=screen.textinput(title=f"{len(correct_states_guess)}/50 States Correct", prompt="What's another state's name?")
    titled_state_guess = state_guess.title()
    if titled_state_guess == "Exit":
        for c_state in correct_states_guess:
           if c_state in states:
                states.remove(c_state)
        # missed_states = {
        #     "Missed States":states
        # }
        df = pandas.DataFrame(states)
        df.to_csv("us-states-game\\states_to_learn.csv")
        break
    if titled_state_guess in states:
            correct_states_guess.append(titled_state_guess)
            correct_guess=us_states_data[us_states_data.state == titled_state_guess]
            state_turtle = Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_turtle.goto(x=float(correct_guess.x),y=float(correct_guess.y))
            state_turtle.write(titled_state_guess)



# states_x=us_states_data.x.to_list()
# states_y=us_states_data.y.to_list()

