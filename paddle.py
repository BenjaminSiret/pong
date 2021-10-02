from turtle import Turtle

MOVE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), y=new_y)
