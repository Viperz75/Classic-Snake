# Snake Game Project
from turtle import Screen, Turtle
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

timmy = Turtle()
win = Screen()
win.setup(width=512, height=512)
win.title('Classic Snake')
win.bgcolor('black')
timmy.hideturtle()


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

timmy.penup()
timmy.hideturtle()
win.bgpic('grass.gif')
win.tracer(0)


#Class Functions
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# KEYPRESS
win.listen()
win.onkey(snake.up, "Up")
win.onkey(snake.down, "Down")
win.onkey(snake.left, "Left")
win.onkey(snake.right, "Right")

tim = Turtle()
tim.hideturtle()
time.sleep(1)

# GAME LOOP
game_is_on = True
while game_is_on:
    win.update()
    time.sleep(0.1)
    snake.move()
    #Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision with Wall
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        game_is_on = False
        scoreboard.game_over()

    #Detect Collisions with Tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


win.exitonclick()
