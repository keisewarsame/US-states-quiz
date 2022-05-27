import turtle
import pandas
from turtle import Turtle, Screen
from correct import Correct

screen = Screen()
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states_data = pandas.read_csv('50_states.csv')
state_list = states_data['state'].tolist()
guesses = []
study = []

total_states = len(state_list)
states_correct = 0
insert = ''
initial_text = "Guess the State"
playing = True

while states_correct < 50:
    answer_state = screen.textinput(title=f"{insert} {initial_text}", prompt="Name a State").title()
    if answer_state in state_list:
        if answer_state not in guesses:
            guesses.append(answer_state)
            states_correct += 1
            insert = f"{states_correct}/{total_states}"
            initial_text = "States Guessed"
            y = int(states_data[states_data.state == answer_state].y)
            x = int(states_data[states_data.state == answer_state].x)

            correct = Correct(x=x, y=y, state=answer_state)
        else:
            pass

    if answer_state == 'Exit':
        break

for guess in state_list:
    if guess not in guesses:
        study.append(guess)

study_sheet = pandas.DataFrame(study)
study_sheet.to_csv("study_sheet")