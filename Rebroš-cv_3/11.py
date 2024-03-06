import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def karticka(x ,y ,text):
    canvas.create_rectangle(x-100,y-40,x+100,y+40,fill="gray")
    canvas.create_text(x, y,text=text,font="arial 14")




for i in range (10):
    karticka(random.randint(50,300),random.randint(50,200), "Python")

canvas.mainloop()