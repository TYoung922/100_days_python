from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_lives = 3
        self.score = 0
        self.end_game = "Game Over"
        self.winner = "You won!"
        self.color("white")
        self.penup()
        self.goto(-100, 290)
        self.write(self.score, False, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 290)
        self.write(self.current_lives, False, align="center", font=("Courier", 40, "normal"))
        self.hideturtle()


    def increase_score(self, block):
        self.clear()

        if block == 'yellow':
            self.score += 1

        elif block == 'green':
            self.score += 3

        elif block == 'orange':
            self.score += 5

        elif block == 'red':
            self.score += 7

        self.goto(-100, 290)
        self.write(self.score, False, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 290)
        self.write(self.current_lives, False, align="center", font=("Courier", 40, "normal"))

    def decrease_life(self):
        self.clear()
        self.current_lives -= 1
        self.goto(-100, 290)
        self.write(self.score, False, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 290)
        self.write(self.current_lives, False, align="center", font=("Courier", 40, "normal"))

    def game_over(self):
        self.clear()
        self.goto(-100, 290)
        self.write(self.score, False, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 290)
        self.write(self.current_lives, False, align="center", font=("Courier", 40, "normal"))
        self.goto(0, 0)
        self.write(self.end_game, False, align="center", font=("Courier", 40, "normal"))

    def player_win(self):
        self.clear()
        self.goto(-100, 290)
        self.write(self.score, False, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 290)
        self.write(self.current_lives, False, align="center", font=("Courier", 40, "normal"))
        self.goto(0, 0)
        self.write(self.winner, False, align="center", font=("Courier", 40, "normal"))








