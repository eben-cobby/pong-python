# import tkinter as tk
import turtle
import random

# set up game window
wn = turtle.Screen()
wn.title("Pong by eben-cobby")
wn.setup(width=800, height=600)
wn.bgcolor("black")

# creating the left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("red")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# creating the right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("blue")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# creating the ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice([-3, 3])
ball.dy = random.choice([-3, 3])

# game rules
game_over = False
winner = None
player1_points = 0
player2_points = 0
max_points = 3

# display score
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.speed(0)
score_display.penup()
score_display.color("white")
score_display.goto(0, 260)


# update score
def score():
    score_display.clear()
    score_display.write(
        "Player 1:{}  Player 2:{}".format(player1_points, player2_points),
        align="center",
        font=("Courier", 18, "normal"),
    )


score()


# paddle movements handling
def left_paddle_up():
    if left_paddle.ycor() < 250:
        left_paddle.sety(left_paddle.ycor() + 20)


def left_paddle_down():
    if left_paddle.ycor() > -250:
        left_paddle.sety(left_paddle.ycor() + -20)


def right_paddle_up():
    if right_paddle.ycor() < 250:
        right_paddle.sety(right_paddle.ycor() + 20)


def right_paddle_down():
    if right_paddle.ycor() > -250:
        right_paddle.sety(right_paddle.ycor() - 20)


# set up keyboard bindings
turtle.listen()
turtle.onkeypress(left_paddle_up, "w")
turtle.onkeypress(left_paddle_down, "s")
turtle.onkeypress(right_paddle_up, "Up")
turtle.onkeypress(right_paddle_down, "Down")

# game loop
while True:
    # start rolling ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # check for ball collision with paddles
    if ball.xcor() in range(-350, -330) and (
        ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50
    ):
        ball.setx(-330)
        ball.dx *= -1
    elif ball.xcor() in range(330, 350) and (
        ball.ycor() < right_paddle.ycor() + 50
        and ball.ycor() > right_paddle.ycor() - 50
    ):
        ball.setx(330)
        ball.dx *= -1

    # check for ball colliding with top or bottom walle
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # check for ball going off screen
    if ball.xcor() > 390:
        player1_points += 1
        score()
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= random.choice([-1, 1])

    elif ball.xcor() < -390:
        player2_points += 1
        score()
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= random.choice([-1, 1])

    # check for game conditions
    if player1_points == max_points:
        game_over = True
        winner = "Player 1"
    elif player2_points == max_points:
        game_over = True
        winner = "Player 2"

    # game over screen
    if game_over == True:
        ball.hideturtle()
        left_paddle.hideturtle()
        right_paddle.hideturtle()
        game_over_display = turtle.Turtle()
        game_over_display.color("white")
        game_over_display.penup()
        game_over_display.hideturtle()
        game_over_display.goto(0, 0)
        game_over_display.write(
            "GAME OVER! {} wins!".format(winner),
            align="center",
            font=("Courier", 30, "normal"),
        )
        break


turtle.done()
