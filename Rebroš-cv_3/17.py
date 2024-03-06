import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()



for i in range(7000):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if y < 90:
        farba = "black"
    elif y < 170:
        farba = "red"
    else:
        farba = "gold"


    canvas.create_oval(x - 5,y - 5,x + 5,y+ 5,fill=farba,width=0)

canvas.mainloop()