from turtle import Turtle

FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 250)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}",align='left',font=FONT)
        self.level += 1

    def game_over(self):
        self.reset()
        self.write("Game Over!" , align='center', font=FONT)
