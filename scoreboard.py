from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("high_score.txt", mode="r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("high_score.txt", mode="w") as file:
                file.write("0")
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
