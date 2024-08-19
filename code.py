import random
import turtle
import time

running = True

wn = turtle.Screen()
wn.title("fruit clickler")
wn.bgcolor("black")
wn.register_shape("luffy.gif")

clicks = 0
reclick = clicks

time_limit = 60
start_time = time.time()

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.up()
pen.clear()

pen.speed(100)
pen.goto(0,400)
pen.write(f"clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

luffy = turtle.Turtle()
luffy.shape("luffy.gif")
luffy.speed(0)
RCo = random.randint(-300,300)
luffy.goto(RCo,RCo)

def clicked(x,y):
    global clicks
    global reclick
    reclick = clicks
    clicks += 1

    pen.clear()
    pen.write(f"clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

    RCo = random.randint(-300,300)
    luffy.goto(RCo,RCo)

    luffy.goto(RCo,RCo)

luffy.onclick(clicked)

while clicks > reclick:
    luffy.onclick(clicked)

    if Time:
        break

print("GAME OVER!")

wn.mainloop()
