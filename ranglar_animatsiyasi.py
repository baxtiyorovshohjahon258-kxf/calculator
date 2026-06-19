from turtle import *
from math import sin, cos, radians

screen = Screen()
screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("Cosmic Mandala Animation")

tracer(0)

t = Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

colors = [
    "red", "orange", "yellow",
    "lime", "cyan", "blue",
    "purple", "magenta"
]

angle_offset = 0
frame = 0

def draw_layer(radius, petals, size, rotation):
    for i in range(petals):
        t.penup()
        t.goto(0, 0)

        angle = (360 / petals) * i + rotation

        x = cos(radians(angle)) * radius
        y = sin(radians(angle)) * radius

        t.goto(x, y)
        t.pendown()

        t.color(colors[i % len(colors)])

        for j in range(36):
            t.forward(size)
            t.left(170)

def draw_star(radius, points, rotation):
    t.penup()
    t.goto(0, 0)
    t.setheading(rotation)
    t.forward(radius)
    t.pendown()

    t.color("white")

    for _ in range(points):
        t.forward(radius)
        t.right(180 - (180 / points))

def draw_ring(radius, circles, rotation):
    for i in range(circles):

        ang = (360 / circles) * i + rotation

        x = cos(radians(ang)) * radius
        y = sin(radians(ang)) * radius

        t.penup()
        t.goto(x, y)
        t.pendown()

        t.color(colors[i % len(colors)])

        t.circle(20)

def draw_spiral(rotation):
    t.penup()
    t.goto(0, 0)
    t.setheading(rotation)
    t.pendown()

    for i in range(80):

        t.color(colors[i % len(colors)])

        t.forward(i * 2)
        t.left(59)

def draw_orbit(radius, count, rotation):

    for i in range(count):

        ang = (360 / count) * i + rotation

        x = cos(radians(ang)) * radius
        y = sin(radians(ang)) * radius

        t.penup()
        t.goto(x, y)
        t.pendown()

        t.color(colors[(i + frame) % len(colors)])

        t.begin_fill()
        t.circle(8)
        t.end_fill()

while True:

    t.clear()

    pulse1 = 150 + sin(radians(frame * 3)) * 40
    pulse2 = 250 + sin(radians(frame * 2)) * 60
    pulse3 = 350 + sin(radians(frame * 4)) * 50

    draw_layer(
        pulse1,
        18,
        40,
        angle_offset
    )

    draw_layer(
        pulse2,
        24,
        30,
        -angle_offset
    )

    draw_layer(
        pulse3,
        30,
        20,
        angle_offset * 2
    )

    draw_ring(
        pulse1,
        24,
        angle_offset
    )

    draw_ring(
        pulse2,
        36,
        -angle_offset 
    )

    draw_orbit(
        pulse3,
        40,
        angle_offset
    )

    draw_star(
        120,
        8,
        angle_offset * 3
    )

    draw_spiral(
        angle_offset
    )

    angle_offset += 2
    frame += 1

    update()

done()


