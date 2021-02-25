# Snake Game Project
from turtle import Screen, Turtle
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

# SCREEN SETUP
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake")
screen.tracer(0)

# Game Name
tim = Turtle()
tim.color("SpringGreen")
tim.write("Classic Snake", align="center", font=("Engravers MT", 35, "normal"))
tim.hideturtle()
time.sleep(1.7)
tim.clear()

# Company Name
tim.color("RoyalBlue2")
tim.write("By Brother's Co.", align="center", font=("Algerian", 40, "normal"))
tim.hideturtle()
time.sleep(2)
tim.clear()

#Class Functions
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# KEYPRESS
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

tim = Turtle()
tim.hideturtle()
time.sleep(1)

# GAME LOOP
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision with Wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    #Detect Collisions with Tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
