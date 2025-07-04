import turtle
import random
import time

# initial setup
delay = 0.1
sc = 0
hs = 0
bodies = []

# Create screen
s1 = turtle.Screen()
s1.title("SNAKE GAME")
s1.bgcolor("light blue")
s1.setup(width=600, height=600)
s1.tracer(0)  # Turn off auto screen updates

# Create head
h1 = turtle.Turtle()
h1.shape("circle")
h1.speed(0)
h1.color("white")
h1.fillcolor("black")
h1.penup()
h1.goto(0, 0)
h1.direction = "stop"

# Create food
f1 = turtle.Turtle()
f1.speed(0)
f1.shape("square")
f1.color("white")
f1.penup()
f1.goto(150, 240)

# Scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.color("black")
sb.penup()
sb.hideturtle()
sb.goto(-270, 260)
sb.write("Score: 0 | Highest Score: 0", font=("Arial", 16, "normal"))

# Game Over Message Turtle
gm = turtle.Turtle()
gm.hideturtle()
gm.penup()
gm.color("red")
gm.goto(0, 0)

# Functions to change direction
def moveup():
    if h1.direction != "down":
        h1.direction = "up"

def moveleft():
    if h1.direction != "right":
        h1.direction = "left"

def moveright():
    if h1.direction != "left":
        h1.direction = "right"

def movedown():
    if h1.direction != "up":
        h1.direction = "down"

def movestop():
    h1.direction = "stop"

# Movement logic
def move():
    x = h1.xcor()
    y = h1.ycor()
    if h1.direction == "up":
        h1.sety(y + 20)
    if h1.direction == "down":
        h1.sety(y - 20)
    if h1.direction == "left":
        h1.setx(x - 20)
    if h1.direction == "right":
        h1.setx(x + 20)

# Keyboard bindings
s1.listen()
s1.onkey(moveup, "Up")
s1.onkey(movedown, "Down")
s1.onkey(moveleft, "Left")
s1.onkey(moveright, "Right")
s1.onkey(movestop, "space")

# Game loop
while True:
    s1.update()

    # Border collision - wraparound
    if h1.xcor() > 290:
        h1.setx(-290)
    if h1.xcor() < -290:
        h1.setx(290)
    if h1.ycor() > 290:
        h1.sety(-290)
    if h1.ycor() < -290:
        h1.sety(290)

    # Food collision
    if h1.distance(f1) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        f1.goto(x, y)

        # Add body part
        b1 = turtle.Turtle()
        b1.speed(0)
        b1.shape("square")
        b1.color("white")
        b1.penup()
        bodies.append(b1)

        # Update score
        sc += 10
        if sc > hs:
            hs = sc
        sb.clear()
        sb.write(f"Score: {sc} | Highest Score: {hs}", font=("Arial", 16, "normal"))
        delay -= 0.001

    # Move body
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)
    if len(bodies) > 0:
        x = h1.xcor()
        y = h1.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with body
    for b in bodies:
        if b.distance(h1) < 20:
            time.sleep(1)
            h1.goto(0, 0)
            h1.direction = "stop"
            for body in bodies:
                body.hideturtle()
            bodies.clear()

            # Show "GAME OVER" message
            gm.clear()
            gm.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
            time.sleep(2)
            gm.clear()  # remove the message after 2 seconds

            # Reset game state
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write(f"Score: {sc} | Highest Score: {hs}", font=("Arial", 16, "normal"))

    time.sleep(delay)
