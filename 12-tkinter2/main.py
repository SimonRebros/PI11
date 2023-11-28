import tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()
x = 3
xx = x
y = 10
d = 30
pocet = 598 // d # //je dve celociselne delnie 7 // 3 = 2
for j in range(498 // d):
    for i in range(pocet):
        farba = random.choice(("green", "red", "blue", "orange", "purple"))
        canvas.create_polygon(x,y+d,x+d//2,y,x+d,y+d,fill=farba)
        canvas.create_rectangle(x,y+d,x+ d,y + 2*d,fill=farba)
        canvas.create_line(x + d // 4, y + d * 1.5, x + d // 1.25, y + d * 1.5)
        canvas.create_rectangle(x+d//4,y+d*1.25,x+d//1.25,y+d*1.75)
        canvas.create_line(x+d//2,y+d*1.25,x+d//2,y+d*1.75)
        x = x + 2*d
    y = y + 2*d
    x = xx





canvas.mainloop()