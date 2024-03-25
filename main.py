import time
from turtle import Screen
from Snake import Snake
from multi import Snake1, Snake2
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake.py")
screen.tracer(0)
app_on = True

while app_on:

    players = screen.textinput("Snake!", "How many players? 1 or 2")

    if players == "exit":
        app_on = False

    elif players == "1":
        snake = Snake()
        food = Food()
        score = Score()
        score.singleplayer()
        food.refresh()

        screen.listen()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")

        game_on = True
        while game_on:
            screen.update()
            time.sleep(0.10)
            snake.move()
            if snake.head.distance(food) < 18:
                food.refresh()
                snake.extend()
                score.increase_score()
            if snake.head.xcor() > 300:
                game_on = False
                score.game_over()
            elif snake.head.xcor() < -320:
                game_on = False
                score.game_over()
            elif snake.head.ycor() > 320:
                game_on = False
                score.game_over()
            elif snake.head.ycor() < -300:
                game_on = False
                score.game_over()

            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    game_on = False
                    score.game_over()

        screen.exitonclick()

    elif players == "2":
        snake1 = Snake1()
        snake2 = Snake2()
        food = Food()
        score = Score()
        score2 = Score()
        score.player1()
        score2.player2()
        food.refresh()

        screen.listen()
        screen.onkey(snake1.up, "Up")
        screen.onkey(snake1.down, "Down")
        screen.onkey(snake1.left, "Left")
        screen.onkey(snake1.right, "Right")
        screen.onkey(snake2.up, "w")
        screen.onkey(snake2.down, "s")
        screen.onkey(snake2.left, "a")
        screen.onkey(snake2.right, "d")

        game_on = True
        while game_on:
            screen.update()
            time.sleep(0.10)
            snake1.move()
            snake2.move()
            if snake1.head.distance(food) < 18:
                food.refresh()
                snake1.extend()
                score.increase_score_p1()
            if snake2.head.distance(food) < 18:
                food.refresh()
                snake2.extend()
                score2.increase_score_p2()
            if snake1.head.xcor() > 300 or snake1.head.xcor() < -320 or snake1.head.ycor() > 320 or snake1.head.ycor() < -300:
                game_on = False
                score.green_win()
            if snake2.head.xcor() > 300 or snake2.head.xcor() < -320 or snake2.head.ycor() > 320 or snake2.head.ycor() < -300:
                game_on = False
                score.white_win()

            for segment in snake1.segments[1:]:
                if snake1.head.distance(segment) < 10:
                    game_on = False
                    score.green_win()
                if snake2.head.distance(segment) < 10:
                    game_on = False
                    score.white_win()
            for segment in snake2.segments[1:]:
                if snake2.head.distance(segment) < 10:
                    game_on = False
                    score.white_win()
                if snake1.head.distance(segment) < 10:
                    game_on = False
                    score.green_win()

        screen.exitonclick()



