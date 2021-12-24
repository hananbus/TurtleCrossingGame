import time
from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = ScoreBoard()
cars = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # level_up
    if player.ycor() > 280:
        player.level_up()
        score.update_score()
        cars.increment_speed()

    # collision with car
    for car in cars.cars:
        if player.distance(car) < 20:
            game_on = False
            score.game_over()

screen.exitonclick()
