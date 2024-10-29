from  turtle import Screen

from pandas.io.sas.sas_constants import block_count_length

from day_55.main import index
from paddle_class import Paddle
from ball_class import Ball
from score_board import Scoreboard
from block_class import BlockGrid
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=700)
screen.title("Breakout")
screen.tracer(0)


player_paddle = Paddle((0, -310))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player_paddle.go_right, "Right")
screen.onkeypress(player_paddle.go_left, "Left")


grid = BlockGrid()

hit_count = 0
red_hit = False
orange_hit = False
hit_four = False
hit_twelve = False


game_is_on = True
still_have_blocks = True
# game_screen = 1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Ball wall collision
    if ball.xcor() < -280 or ball.xcor() > 280:
        ball.bounce()

    #Ball top collision
    if ball.ycor() > 330:
        ball.top_bounce()


    #detect collision with paddle
    # if ball.distance(player_paddle) < 50 and ball.ycor()  < -280:
    #     ball.hit()
    if 25 < ball.distance(player_paddle) < 50 and ball.ycor() < -280:
        ball.hit(2)
    elif ball.distance(player_paddle) < 25 and ball.ycor() < -280:
        ball.hit(1)

    #detect collision with block
    index, color = grid.detect_collision(ball)
    if index is not None:
        ball.top_bounce()
        scoreboard.increase_score(color)
        hit_count += 1

        screen.update()

        if not grid.out_of_blocks():
            still_have_blocks = False
            game_is_on = False
            scoreboard.player_win()

    if hit_count == 4 and not hit_four:
        ball.increase_speed()
        print(f"ball speed {ball.move_speed}")
        hit_four = True

    if hit_count == 12 and not hit_twelve:
        ball.increase_speed()
        print(f"ball speed {ball.move_speed}")
        hit_twelve = True

    if color == 'red' and not red_hit:
        ball.increase_speed()
        print(f"red, hit ball speed {ball.move_speed}")
        red_hit = True

    if color == 'orange' and orange_hit == False:
        if color == 'orange':
            ball.increase_speed()
            print(f"orange hit ball speed {ball.move_speed}")
            orange_hit = True



#detect if life lost
    if ball.ycor() < -330:
        hit_count = 0
        red_hit = False
        orange_hit = False
        hit_four = False
        hit_twelve = False
        color = None
        ball.reset_position()
        scoreboard.decrease_life()
        print(hit_count)

    if scoreboard.current_lives == 0:
        game_is_on = False
        scoreboard.game_over()



    # if grid.out_of_blocks():
    #     still_have_blocks = False
    # else:
    #     still_have_blocks = True
    #
    # if not still_have_blocks:
    #     game_is_on = False
    #     scoreboard.player_win()




print("Game Over")












screen.exitonclick()