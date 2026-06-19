from turtle import *
from random import randint
from math import sin, cos, radians

# screen = Screen()
# screen.setup(1000, 800)
# screen.bgcolor("black")
# screen.title("Black Hole Simulation")

# tracer(0)

# t = Turtle()
# t.hideturtle()
# t.speed(0)

# particles = []

# colors = [
#     "#00ffff",
#     "#00ccff",
#     "#0099ff",
#     "#6666ff",
#     "#9933ff",
#     "#cc00ff",
#     "#ff00cc",
# ]

# # Boshlang'ich zarrachalar
# for _ in range(400):
#     particles.append({
#         "angle": randint(0, 360),
#         "radius": randint(50, 420),
#         "speed": randint(1, 5) / 10,
#         "size": randint(2, 6)
#     })

# frame = 0

# while True:

#     t.clear()

#     # Qora tuynuk markazi
#     t.penup()
#     t.goto(0, -40)
#     t.color("white")
#     t.begin_fill()
#     t.circle(40)
#     t.end_fill()

#     # Akkretsion disk (yorug' halqa)
#     for ring in range(5):

#         t.penup()
#         t.goto(0, -(70 + ring * 4))
#         t.color(colors[(ring + frame // 5) % len(colors)])
#         t.pendown()
#         t.circle(70 + ring * 4)

#     # Zarrachalar
#     for p in particles:

#         p["angle"] += p["speed"]
#         p["radius"] -= 0.25

#         if p["radius"] < 10:
#             p["radius"] = randint(300, 450)
#             p["angle"] = randint(0, 360)

#         x = cos(radians(p["angle"])) * p["radius"]
#         y = sin(radians(p["angle"])) * p["radius"]

#         color_index = int(
#             (p["radius"] / 450) * (len(colors) - 1)
#         )

#         t.penup()
#         t.goto(x, y)
#         t.dot(
#             p["size"],
#             colors[color_index]
#         )

#     frame += 1

#     update()

# done()

# 
import random
from turtle import *
from random import randint, uniform
from math import sin, cos, radians

# =========================
# WINDOW
# =========================

WIDTH = 1200
HEIGHT = 900
  
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Black Hole - Stage 1")

tracer(0)

t = Turtle()
t.hideturtle()
t.speed(0)

# =========================
# STARS
# =========================

stars = []

for _ in range(400):

    stars.append(
        (
            randint(-600, 600),
            randint(-450, 450),
            randint(1, 3)
        )
    )

# =========================
# DISK PARTICLES
# =========================

particles = []

for _ in range(1200):

    radius = uniform(100, 320)

    particles.append({
        "radius": radius,
        "angle": uniform(0, 360),

        # ichki qismi tezroq
        "speed": 0.4 + ((320 - radius) / 70),

        "size": randint(2, 4)
    })

# =========================
# COLORS
# =========================

gold = [
    "#fffde7",
    "#fff9c4",
    "#fff59d",
    "#fff176",
    "#ffee58",
    "#fdd835",
    "#fbc02d",
    "#f9a825",
    "#ff8f00"
]

# =========================
# DRAW STARS
# =========================

def draw_stars():

    for sx, sy, size in stars:

        t.penup()
        t.goto(sx, sy)

        if size == 1:
            t.dot(size, "#888888")
        elif size == 2:
            t.dot(size, "#cccccc")
        else:
            t.dot(size, "white")

# =========================
# EVENT HORIZON
# =========================

def draw_event_horizon():

    t.penup()
    t.goto(0, -80)

    t.color("black")

    t.begin_fill()
    t.circle(80)
    t.end_fill()

# =========================
# PHOTON RING
# =========================

def draw_photon_ring():

    t.penup()
    t.goto(0, -88)

    t.pencolor("#fff59d")
    t.pensize(4)

    t.pendown()
    t.circle(88)
    t.penup()

# =========================
# GLOW
# =========================

def draw_glow(frame):

    pulse = 3 + sin(radians(frame * 4)) * 2

    for i in range(10):

        t.penup()

        r = 90 + i * 3

        t.goto(0, -r)

        t.pencolor(
            gold[
                min(
                    i,
                    len(gold) - 1
                )
            ]
        )

        t.pensize(
            pulse + i * 0.2
        )

        t.pendown()
        t.circle(r)

# =========================
# ACCRETION DISK
# =========================

def draw_disk(frame):

    for p in particles:

        p["angle"] += p["speed"]

        angle = p["angle"]
        radius = p["radius"]

        x = cos(
            radians(angle)
        ) * radius

        y = sin(
            radians(angle)
        ) * radius * 0.35

        idx = int(
            ((320 - radius) / 220)
            * (len(gold) - 1)
        )

        idx = max(
            0,
            min(idx, len(gold) - 1)
        )

        t.penup()
        t.goto(x, y)

        t.dot(
            p["size"],
            gold[idx]
        )

# =========================
# OUTER DISK RINGS
# =========================

def draw_disk_rings():

    for ring in range(100, 320, 25):

        t.penup()
        t.goto(0, -ring * 0.35)

        t.pencolor(
            gold[
                (ring // 25)
                % len(gold)
            ]
        )

        t.pensize(1)

        t.pendown()

        for a in range(361):

            x = cos(
                radians(a)
            ) * ring

            y = sin(
                radians(a)
            ) * ring * 0.35

            t.goto(x, y)

        t.penup()

# =========================
# MAIN LOOP
# =========================

frame = 0

while True:

    t.clear()

    draw_stars()

    draw_disk(frame)

    draw_disk_rings()

    draw_glow(frame)

    draw_event_horizon()

    draw_photon_ring()

    update()

    frame += 1

    done()
    def draw_disk(frame):

        for p in particles:

        # Aylanish
            p["angle"] += p["speed"]

        # Markazga tortilish
            p["radius"] -= 0.05

            if p["radius"] < 90:

                p["radius"] = uniform(250, 320)
                p["angle"] = uniform(0, 360)

            angle = p["angle"]
            radius = p["radius"]

            x = cos(radians(angle)) * radius
            y = sin(radians(angle)) * radius * 0.35

        # ---------------------
        # Gravitational Lensing
        # ---------------------

            if y > 0:

                lens = (1 - radius / 350)

                y += 35 * lens

        # ---------------------
        # Doppler Brightening
        # ---------------------

            brightness = (
                cos(radians(angle))
                + 1
            ) / 2

            idx = int(
                ((320 - radius) / 220)
                * (len(gold) - 1)
            )

            idx = max(
                0,
                min(idx, len(gold) - 1)
            )

            size = p["size"]

            if brightness > 0.7:
                size += 2

            elif brightness > 0.4:
                size += 1

            t.penup()
            t.goto(x, y)

            t.dot(
                size,
                gold[idx]
            )
    def draw_shadow():

        t.penup()
        t.goto(0, -95)

        t.color("black")
        t.begin_fill()
        t.circle(95)
        t.end_fill()
    from turtle import *
    from random import uniform, randint
    from math import sin, cos, radians, sqrt

# =========================
# SCREEN
# =========================

    screen = Screen()
    screen.setup(1200, 900)
    screen.bgcolor("black")
    screen.title("FINAL BLACK HOLE - CINEMATIC")
    tracer(0)

    t = Turtle()
    t.hideturtle()
    t.speed(0)

# =========================
# STARS
# =========================

    stars = [
        (randint(-600, 600), randint(-450, 450), randint(1, 3))
        for _ in range(500)
    ]

# =========================
# GOLD COLORS
# =========================

    gold = [
        "#fffde7", "#fff9c4", "#fff59d",
        "#fff176", "#ffee58", "#fdd835",
        "#fbc02d", "#f9a825", "#ff8f00"
    ]

# =========================
# PARTICLES (DISK)
# =========================

    particles = []

    for _ in range(1800):

        r = uniform(100, 360)

        particles.append({
            "r": r,
            "a": uniform(0, 360),
            "speed": 0.3 + (360 - r) / 120,
            "size": randint(2, 4),
            "layer": 1 if random.random() > 0.5 else -1
        })

# =========================
# CAMERA WOBBLE
# =========================

    def camera_offset(frame):

        x = sin(radians(frame * 1.5)) * 6
        y = cos(radians(frame * 1.2)) * 4

        return x, y

# =========================
# STARS (GRAVITY DISTORTION)
# =========================

    def draw_stars(frame, cx, cy):

        for x, y, s in stars:

            dx = x - cx
            dy = y - cy

            dist = sqrt(dx*dx + dy*dy)

        # lensing
            factor = 1 + 200 / (dist + 50)

            sx = dx * factor * 0.3
            sy = dy * factor * 0.3

            t.penup()
            t.goto(sx, sy)

            t.dot(s, "white")

# =========================
# EVENT HORIZON
# =========================

    def draw_horizon():

        t.penup()
        t.goto(0, -90)

        t.color("black")
        t.begin_fill()
        t.circle(90)
        t.end_fill()

# =========================
# PHOTON RING
# =========================

    def draw_photon(frame):

        t.penup()
        t.goto(0, -98)

        t.pensize(3)
        t.pencolor("#fff59d")

        t.pendown()
        t.circle(98)
        t.penup()

# =========================
# ENERGY FLARES
# =========================

    def draw_flares(frame):

        for i in range(120):

            y = i * 5 - 300
            x = sin(radians(frame * 3 + i)) * 20

            t.penup()
            t.goto(x, y)
            t.dot(3, "#80d8ff")

            t.penup()
            t.goto(-x, -y)
            t.dot(3, "#80d8ff")

# =========================
# DISK (FULL CINEMATIC PHYSICS)
# =========================

    def draw_disk(frame, cx, cy):

        spin = frame * 2

        for p in particles:

            p["a"] += p["speed"]
            p["r"] -= 0.05

            if p["r"] < 90:
                p["r"] = uniform(280, 360)
                p["a"] = uniform(0, 360)

            a = p["a"] + spin
            r = p["r"]

            x = cos(radians(a)) * r
            y = sin(radians(a)) * r * 0.35

        # =========================
        # WARP DISTORTION (GRAVITY LENS)
        # =========================

            dist = sqrt(x*x + y*y)

            warp = 120 / (dist + 80)

            x *= (1 + warp * 0.15)
            y *= (1 + warp * 0.10)

        # =========================
        # CAMERA OFFSET
        # =========================

            ox, oy = camera_offset(frame)

            x += ox
            y += oy

        # =========================
        # DEPTH LAYER (front/back disk)
        # =========================

            if p["layer"] == 1:
                y += 10
            else:
                y -= 10

        # =========================
        # DOPPLER BRIGHTNESS
        # =========================

            doppler = (cos(radians(a)) + 1) / 2

            idx = int(((360 - r) / 260) * (len(gold) - 1))
            idx = max(0, min(idx, len(gold) - 1))

            size = p["size"]

            if doppler > 0.7:
                size += 2

            t.penup()
            t.goto(x, y)
            t.dot(size, gold[idx])

# =========================
# GLOW RINGS
# =========================

    def draw_glow(frame):

        pulse = sin(radians(frame * 4)) * 4

        for i in range(8):

            t.penup()
            t.goto(0, -100 - i * 4)

            t.pensize(2 + pulse + i * 0.3)
            t.pencolor(gold[i % len(gold)])

            t.pendown()
            t.circle(100 + i * 4)

            t.penup()

# =========================
# MAIN LOOP
# =========================

    frame = 0

    while True:

        t.clear()

        cx, cy = camera_offset(frame)

        draw_stars(frame, cx, cy)

        draw_disk(frame, cx, cy)

        draw_glow(frame)

        draw_flares(frame)

        draw_photon(frame)

        draw_horizon()

        update()

        frame += 1

        done()       