
from turtle import Turtle

FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Level = {self.score}", align="left", font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align ="center", font=("Arial", 25, "bold"))