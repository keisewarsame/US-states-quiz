from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class Correct(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(x, y)
        self.write(f'{state}', font=FONT)