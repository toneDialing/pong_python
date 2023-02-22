# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import os

window = turtle.Screen()
window.title("Pong by @TokyoEdTech")
window.bgcolor("black")
window.setup(width=800, height=600) # (0, 0) is center of screen
window.tracer(0)

# Scores
score_left = 0
score_right = 0
# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(0, 260)
scoreboard.write("Player A: {} Player B: {}".format(score_left, score_right),
    align="center", font=("Courier", 24, "normal"))
# Winner display
winner_banner = turtle.Turtle()
winner_banner.hideturtle()
winner_banner.speed(0)
winner_banner.color("white")
winner_banner.penup()
winner_banner.goto(0, 200)
# Play again display (not yet functional)
play_again_banner = turtle.Turtle()
play_again_banner.hideturtle()
play_again_banner.speed(0)
play_again_banner.color("white")
play_again_banner.penup()
play_again_banner.goto(0, -240)
# Left paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.color("white")
paddle_left.penup()
paddle_left.goto(-350, 0)
# Right paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color("white")
paddle_right.penup()
paddle_right.goto(350, 0)
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

window.listen()
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_up, "W")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_left_down, "S")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")

# Play opening sound in full before game starts
window.update()
os.system("afplay start.wav")

# Every game needs a main game loop, where the whole game is executed
# Main game loop
while score_left<3 and score_right<3:
    window.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce off top/bottom walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    # Score on left/right walls
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -2
        ball.dy = -2
        score_left += 1
        scoreboard.clear()
        scoreboard.write("Player A: {} Player B: {}".format(score_left, score_right),
            align="center", font=("Courier", 24, "normal"))
        if score_left<3:
            os.system("afplay score.wav&")
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 2
        ball.dy = 2
        score_right += 1
        scoreboard.clear()
        scoreboard.write("Player A: {} Player B: {}".format(score_left, score_right),
            align="center", font=("Courier", 24, "normal"))
        if score_right<3:
            os.system("afplay score.wav&")
    # Collide with paddles
    if ((ball.xcor()>340 and ball.xcor()<350) and
    (ball.ycor()<(paddle_right.ycor()+45) and ball.ycor()>(paddle_right.ycor()-45))):
        ball.setx(340)
        ball.dx *= -1.2
        ball.dy *= 1.2
        os.system("afplay bounce.wav&")
    if ((ball.xcor()<-340 and ball.xcor()>-350) and
    (ball.ycor()<(paddle_left.ycor()+45) and ball.ycor()>(paddle_left.ycor()-45))):
        ball.setx(-340)
        ball.dx *= -1.2
        ball.dy *= 1.2
        os.system("afplay bounce.wav&")

window.update()
if score_left>=3:
    winner_banner.write("Player A wins!", align="center", font=("Courier", 32, "bold"))
if score_right>=3:
    winner_banner.write("Player B wins!", align="center", font=("Courier", 32, "bold"))
window.update()
os.system("afplay win.wav")

# Play again feature isn't working yet
# play_again_banner.write("Press 'p' to play again", align="center", font=("Courier", 24, "normal"))

while True:
    window.update()