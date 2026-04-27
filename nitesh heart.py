import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.title("Heart for Nitesh")
screen.bgcolor("white")

# Create turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.color("#C4BFC0")  
t.pensize(3)

# Move to starting position
t.penup()
t.goto(0, -100)
t.pendown()

# Draw heart using parametric equation
# x = 16 sin^3(t), y = 13 cos(t) - 5 cos(2t) - 2 cos(3t) - cos(4t)
# We'll scale and center it nicely
scale = 10
t.begin_fill()
for deg in range(361):
    rad = math.radians(deg)
    x = scale * 16 * (math.sin(rad) ** 3)
    y = scale * (13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad))
    if deg == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)
t.end_fill()

# Write name in the center
t.penup()
t.color("white")
t.goto(0, -10)  # adjust vertical position if needed
t.write("nitesh", align="center", font=("Arial", 28, "bold"))

# Keep window open
turtle.done()

