import tkinter
canvas = tkinter.Canvas()
canvas.pack()
stlpce = int(input("zadaj pocet stlpcov: "))
riadky = int(input("zadaj pocet riadkov"))
farba1, farba2 = "maroon", "gold"
x = 5
y = 5


vel = 30
for i in range(stlpce):
    for j in range(riadky):
        canvas.create_rectangle(x, y, x + 30,y + 30,fill = farba1 )
        farba1, farba2 = farba2, farba1
        x = x + 35
    y = y + 35
    x = 5




canvas.mainloop()