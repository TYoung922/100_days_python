from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("aqua")
        self.penup()
        self.x_move = 1
        self.y_move = -10
        self.move_speed = 0.075

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.x_move *= -1

    # def hit(self):
    #     self.y_move *= -1
    def hit(self, spot):
        if spot == 1:
            if self.x_move == 10 or self.x_move == 15 or self.x_move == 1:
                self.x_move = 10
            elif self.x_move == -10 or self.x_move == -15 or self.x_move == -1:
                self.x_move = -10
        else:
            if self.x_move == 10 or self.x_move == 15 or self.x_move == 1:
                self.x_move = 15
            elif self.x_move == -10 or self.x_move == -15 or self.x_move == -1:
                self.x_move = -15
        self.y_move *= -1


    def top_bounce(self):
        self.y_move *= -1
        # self.x_move *= -1


    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.075
        # self.y_move *= -1
        self.x_move = 10

    def increase_speed(self):
        self.move_speed *= 0.6