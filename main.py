import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#Remember to do this after the screen.tracer(0) otherwise the turtle will move to the position rather than be there,
# so the screen.tracer (0) and the screen.update() function handle that

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Enabling the turtle to move up when pressing the up key
screen.listen()
screen.onkey(player.move_up, "Up")

#Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()
