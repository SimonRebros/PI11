import tkinter
x = 10
y = 2
z = 2
q = 10
dlzka = 498
medzera = 30
farba1 = "red"
farba2 = "blue"
canvas = tkinter.Canvas(height=500,width=500)
canvas.pack()
for i in range(30):
    canvas.create_line(x,y,x ,y + dlzka,width = 5,fill=farba1)
    canvas.create_line(z,q,z + dlzka,q,width = 5,fill=farba1)
    q = q + medzera
    x = x + medzera
    farba1 , farba2 = farba2 , farba1

canvas.mainloop()