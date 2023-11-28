import tkinter
canvas = tkinter.Canvas()
canvas.pack()

x = 5
y = 5
d = 10
r = "red"
b = "blue"
yellow = "yellow"

canvas.create_rectangle(x, y , x + d, y + d,)
canvas.create_rectangle(x + d, y + d , x + 2 * d, y + 2 * d,)
canvas.create_rectangle(x + 2 * d, y + 2 * d , x + 3 * d, y + 3 * d,)
canvas.create_rectangle(x + 3 * d, y + 2 * d , x + 4 * d, y + d,)
canvas.create_rectangle(x + 4 * d, y + d , x + 5 * d, y,)
canvas.create_rectangle(x + d, y + 3 * d , x + 2 * d, y + 4 * d)
canvas.create_rectangle(x + 2 * d, y + 2 * d , x + 3 * d, y + 3 * d)
canvas.create_rectangle(x , y + 4 * d , x + d, y + 5 * d)
canvas.create_rectangle(x + 3 * d, y + 3 * d , x + 4 * d, y + 4 * d)
canvas.create_rectangle(x + 4 * d, y + 4 * d , x + 5 * d, y + 5 * d)

x = 6 * d
y = 5
d = 10
r = "red"
b = "blue"
yellow = "yellow"

canvas.create_rectangle(x, y , x + d, y + d,)
canvas.create_rectangle(x + d, y + d , x + 2 * d, y + 2 * d,)
canvas.create_rectangle(x + 2 * d, y + 2 * d , x + 3 * d, y + 3 * d,)
canvas.create_rectangle(x + 3 * d, y + 2 * d , x + 4 * d, y + d,)
canvas.create_rectangle(x + 4 * d, y + d , x + 5 * d, y,)
canvas.create_rectangle(x + d, y + 3 * d , x + 2 * d, y + 4 * d)
canvas.create_rectangle(x + 2 * d, y + 2 * d , x + 3 * d, y + 3 * d)
canvas.create_rectangle(x , y + 4 * d , x + d, y + 5 * d)
canvas.create_rectangle(x + 3 * d, y + 3 * d , x + 4 * d, y + 4 * d)
canvas.create_rectangle(x + 4 * d, y + 4 * d , x + 5 * d, y + 5 * d)


canvas.mainloop()