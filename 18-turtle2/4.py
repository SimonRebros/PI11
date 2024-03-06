import turtle



t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
turtle.delay(0)
t3.penup()
t3.setpos(0,100)
t3.pendown()
t1.penup()

t1.setpos(-100,0)
t1.pendown()
t2.penup()
t2.setpos(100,0)
t2.pendown()

def stvorec(dlzka):
    for i in range(4):
        t1.fd(dlzka)
        t2.fd(dlzka)
        t3.fd(dlzka)
        t1.left(90)
        t2.left(90)
        t3.left(90)
for i in range(20):
    stvorec(100)
    t1.left((360/20))
    t2.left((360 / 20))
    t3.left((360 / 20))


turtle.mainloop()