import tkinter,time,random
canvas = tkinter.Canvas()
canvas.pack()

stvorec1 = canvas.create_rectangle(10,10,110,110,fill="red")
for i in range(1000):
    canvas.update()
    time.sleep(0.01)
    farba = random.choice(("red","green","orange","purple"))
    canvas.move(stvorec1,1,0) # stvorec1,je objekt ktory sa bude posuvat,100 je o kolko posunut na xovej osi 0 je o kolko posunut na ylonovej osi
    canvas.itemconfig(stvorec1, fill=farba)

canvas.mainloop()
