import tkinter,time,random


canvas_width = 500
canvas_height = 600
santa_x = canvas_width // 2
santa_y = 66
santa_z = canvas_height - 66
santa_posun = 1
santa_2_posun = -1

canvas = tkinter.Canvas(width=canvas_width,height=canvas_height)
canvas.pack()

image_santa = tkinter.PhotoImage(file="santa.png.png")
santa = canvas.create_image(santa_x,santa_y,image=image_santa)
santa_2 = canvas.create_image(santa_y,santa_z,image=image_santa)

while True:
    canvas.update()
    time.sleep(0.001)
    canvas.move(santa,0,santa_posun)
    canvas.move(santa_2, 0, santa_2_posun)
    santa_z = santa_z - santa_2_posun
    santa_y = santa_y + santa_posun
    if santa_y == canvas_height + 64:
        canvas.delete(santa)

        santa_y = 66
        santa = canvas.create_image(santa_x, santa_y, image=image_santa)

    if santa_z == - 64:
        canvas.delete(santa_2)
        santa_z = canvas_height - 66
        santa_2 = canvas.create_image(santa_y, santa_z, image=image_santa)












