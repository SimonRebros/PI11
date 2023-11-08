import tkinter

canvas = tkinter.Canvas()
canvas.pack()
x = 2
y = 2
dlzka = 20
canvas.create_rectangle(x, y, x + dlzka, y + dlzka, fill="red")
canvas.create_rectangle(x + dlzka, y, x + (2*dlzka), y + dlzka, fill="blue")
canvas.create_rectangle(x + (2*dlzka), y, x + (3*dlzka), y + dlzka, fill="green")
canvas.create_oval(x + dlzka, y + dlzka, x + (2*dlzka), y + (2*dlzka), fill="pink")
canvas.create_oval(x + dlzka, y + (2*dlzka), x + (2*dlzka), y + (3*dlzka),fill="yellow")
canvas.create_rectangle(x + dlzka, y + (3*dlzka), x + (2*dlzka), y + (4*dlzka), fill="black")
canvas.create_rectangle(x, y + (3*dlzka), x + dlzka, y + (4*dlzka), fill="purple")
canvas.create_rectangle(x + (2*dlzka), y + (3*dlzka), x + (3*dlzka), y + (4*dlzka), fill="grey")
canvas.mainloop()
