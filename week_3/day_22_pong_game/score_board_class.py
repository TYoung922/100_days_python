from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.color("white")
        self.penup()
        self.goto(-100, 200)
        self.write(self.score_left, False, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, False, align="center", font=("Courier", 80, "normal"))
        self.hideturtle()


    def increase_score_right(self):
        self.clear()
        self.score_right += 1
        self.goto(-100, 200)
        self.write(self.score_left, False, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, False, align="center", font=("Courier", 80, "normal"))

    def increase_score_left(self):
        self.clear()
        self.score_left += 1
        self.goto(-100, 200)
        self.write(self.score_left, False, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, False, align="center", font=("Courier", 80, "normal"))






