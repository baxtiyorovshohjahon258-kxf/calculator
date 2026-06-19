from turtle import*
import random 

bgcolor("black")
speed(0)
hideturtle()

colors = ["lime", "green","red", "yellow","purple"]

for i in range(2000):
    penup()
    x=random.randint(-575,300)
    y=random.randint(-300,575)
    goto(x,y)

    pencolor(random.choice(colors))

    text=random.choice([
        "shohjahon_1st"
        "ACCESS"
        "HACK"
        "SYSTEM"
        "ERROR"
        "ROOT"
        "189"
        "00000"
    ])
    write(text,font=("Courier", 12,"bold"))    

done()