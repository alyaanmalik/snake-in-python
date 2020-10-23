import turtle
import time
import random

delay = 0.1

score = 0
highscore = 0

wn = turtle.Screen()
wn.title("Snake game Python")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.shape("square")
snakehead.color("black")
snakehead.penup()
snakehead.goto(0,0)
snakehead.direction = "stop"

snakefood = turtle.Turtle()
snakefood.speed(0)
snakefood.shape("circle")
snakefood.color("red")
snakefood.penup()
snakefood.goto(0,100)

segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

def goup():
    if snakehead.direction != "down":
        snakehead.direction = "up"
def godown():
    if snakehead.direction != "up":
        snakehead.direction = "down"
def goleft():
    if snakehead.direction != "right":
        snakehead.direction = "left"
def goright():
    if snakehead.direction != "left":
        snakehead.direction = "right"
def move():
    if snakehead.direction == "up":
        y = snakehead.ycor()
        snakehead.sety(y + 20)

    if snakehead.direction == "down":
        y = snakehead.ycor()
        snakehead.sety(y - 20)

    if snakehead.direction == "left":
        x = snakehead.xcor()
        snakehead.setx(x - 20)
    
    if snakehead.direction == "right":
        x = snakehead.xcor()
        snakehead.setx(x + 20)

wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goright, "d")
wn.onkeypress(goleft, "a")

while True:
    wn.update()

    if snakehead.xcor()>290 or snakehead.xcor()<-290 or snakehead.ycor()>290 or snakehead.ycor()<-290:
        time.sleep(1)
        snakehead.goto(0,0)
        snakehead.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
            
        segments.clear()

        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal"))

    if snakehead.distance(snakefood) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snakefood.goto(x,y)

        newsegment = turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape("square")
        newsegment.color("grey")
        newsegment.penup()
        segments.append(newsegment)

        delay -= 0.001
        score += 10

        if score > highscore:
            highscore = score
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal"))
    
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        segments[0].goto(x,y)
    
    move()

    for segment in segments:
        if segment.distance(snakehead) < 20:
            time.sleep(1)
            snakehead.goto(0,0)
            snakehead.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)

wn.mainloop()

