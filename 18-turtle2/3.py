import turtle
import random

t = turtle.Turtle()
turtle.delay(0)

def obluk(d):
    for i in range(9):
        t.fd(d)
        t.lt(10)

def lupen(d):
    for i in range(2):
        obluk(d)
        t.left(90)

def kvet(n,d):
    for j in range(4):
        for i in range(n):



            t.fillcolor(random.choice(("red", "orange","blue","green","black","yellow","pink")))
            t.begin_fill()
            lupen(d)
            t.end_fill()
            t.left(360 / n)
        t.pu()
        t.fd(100)
        t.lt(90)
        t.pd()
kvet(20,10)


turtle.mainloop()