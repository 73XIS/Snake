from turtle import Turtle


class Score(Turtle):
    def singleplayer(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.high_score = 0
        self.speed("fastest")
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score = {self.score}", align="center", font=("Courier", 18, "normal"))

    def player1(self):
        super().__init__()
        self.p1score = 0
        self.penup()
        self.speed("fastest")
        self.goto(-100, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Player 1: {self.p1score}", align="center", font=("Courier", 18, "normal"))

    def player2(self):
        super().__init__()
        self.p2score = 0
        self.penup()
        self.speed("fastest")
        self.goto(100, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Player 2: {self.p2score}", align="center", font=("Courier", 18, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align="center", font=("Courier", 18, "normal"))

    def increase_score_p1(self):
        self.clear()
        self.p1score += 1
        self.write(f"Player 1: {self.p1score}", align="center", font=("Courier", 18, "normal"))

    def increase_score_p2(self):
        self.clear()
        self.p2score += 1
        self.write(f"Player 2: {self.p2score}", align="center", font=("Courier", 18, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Courier", 30, "normal"))

    def white_win(self):
        self.goto(0, 0)
        self.write("Player 1 Wins.", align="center", font=("Courier", 30, "normal"))

    def green_win(self):
        self.goto(0, 0)
        self.write("Player 2 Wins.", align="center", font=("Courier", 30, "normal"))

    def draw(self):
        self.goto(0, 0)
        self.write("Draw!", align="center", font=("Courier", 30, "normal"))
