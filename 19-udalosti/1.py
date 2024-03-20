import tkinter

def tahaj(event):
    x, y = event.x, event.y
    canvas.create_oval(x-10, y-10, x+10, y+10, fill='red')
def klik(event):
    x, y = event.x,event.y
    canvas.create_oval(x - 20,y - 20,x + 20,y + 20,fill = "blue")

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<B1-Motion>', tahaj)
canvas.bind("<ButtonPress>",klik)

tkinter.mainloop()
