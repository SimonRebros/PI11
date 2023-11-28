import tkinter
canvas = tkinter.Canvas(width=900, height=500)
canvas.pack()

x = 5
xx=x
y = 5
d = 5
dlzka = 7*d
vyska = 7*d

r = "red"
b = "black"
yellow = "yellow"
pocet = 898 // dlzka # //je dve celociselne delnie 7 // 3 = 2
for j in range(498 // vyska):
    for i in range(pocet):
        canvas.create_rectangle(x + d, y , x +  2 * d, y + d,fill=b)
        canvas.create_rectangle(x , y + d , x + d, y + 2 * d,fill=b)
        canvas.create_rectangle(x , y + 2 * d , x +  d, y + 3 * d,fill=b)
        canvas.create_rectangle(x + 2 * d, y + 3 * d , x + 3 * d, y + 4 * d,fill=b)
        canvas.create_rectangle(x + 2 * d, y + 6 * d , x + 3 * d, y + 7 * d,fill=b)
        canvas.create_rectangle(x + 4 * d, y + d , x + 5 * d, y,fill=b)
        canvas.create_rectangle(x + d, y + 6 * d , x + 2 * d, y + 7 * d,fill=b)
        canvas.create_rectangle(x + d, y + 3 * d , x + 2 * d, y + 4 * d,fill=b)
        canvas.create_rectangle(x + 2 * d, y  , x + 3 * d, y +  d,fill=b)
        canvas.create_rectangle(x , y + 6 * d , x + d, y + 7 * d,fill=b)
        canvas.create_rectangle(x + 3 * d, y + 3 * d , x + 4 * d, y + 4 * d,fill=b)
        canvas.create_rectangle(x + 3 * d, y + 6 * d , x + 4 * d, y + 7 * d,fill=b)
        canvas.create_rectangle(x + 3 * d, y    , x + 4 * d, y +  d,fill=b)
        canvas.create_rectangle(x + 4 * d, y + 4 * d , x + 5 * d, y + 5 * d,fill=b)
        canvas.create_rectangle(x + 4 * d, y + 5 * d , x + 5 * d, y + 6 * d,fill=b)

        x = 6 * d

        r = "red"
        b = "black"
        yellow = "yellow"

        canvas.create_rectangle(x, y , x + d, y + d,fill=b)
        canvas.create_rectangle(x + d, y  , x + 2 * d, y + d,fill=b)
        canvas.create_rectangle(x + 2 * d, y  , x + 3 * d, y +  d,fill=b)
        canvas.create_rectangle(x +  d, y +  d , x + 2 * d, y + 2*d,fill=b)
        canvas.create_rectangle(x + d, y + 3 * d , x + 2 * d, y + 4 * d,fill=b)
        canvas.create_rectangle(x +  d, y + 2 * d , x + 2 * d, y + 3 * d,fill=b)
        canvas.create_rectangle(x +d, y + 4 * d , x + 2*d, y + 5 * d,fill=b)
        canvas.create_rectangle(x +d, y + 5 * d , x + 2*d, y + 6 * d,fill=b)
        canvas.create_rectangle(x +d, y + 6 * d , x + 2*d, y + 7 * d,fill=b)
        canvas.create_rectangle(x  , y + 6 * d , x +  d, y + 7 * d,fill=b)
        canvas.create_rectangle(x +2*d , y + 6 * d , x + 3* d, y + 7 * d,fill=b)

        x = 10 * d


        b = "black"

        canvas.create_rectangle(x, y , x + d, y + d,fill=b)
        canvas.create_rectangle(x + d, y +d , x + 2 * d, y + 2*d,fill=b)
        canvas.create_rectangle(x + 3*d, y +d , x + 4 * d, y + 2*d,fill=b)
        canvas.create_rectangle(x + 2 * d, y +3*d , x + 3 * d, y + 4* d,fill=b)
        canvas.create_rectangle(x , y +  d , x +  d, y + 2*d,fill=b)
        canvas.create_rectangle(x , y + 3 * d , x +  d, y + 4 * d,fill=b)
        canvas.create_rectangle(x , y + 2 * d , x +  d, y + 3 * d,fill=b)
        canvas.create_rectangle(x , y + 4 * d , x + d, y + 5 * d,fill=b)
        canvas.create_rectangle(x , y + 5 * d , x + d, y + 6 * d,fill=b)
        canvas.create_rectangle(x +4*d, y + 6 * d , x + 5*d, y + 7 * d,fill=b)
        canvas.create_rectangle(x +4*d, y + 5 * d , x + 5*d, y + 6 * d,fill=b)
        canvas.create_rectangle(x +4*d, y + 4 * d , x + 5*d, y + 5 * d,fill=b)
        canvas.create_rectangle(x +4*d, y + 3 * d , x + 5*d, y + 4 * d,fill=b)
        canvas.create_rectangle(x +4*d, y + 2 * d , x + 5*d, y + 3 * d,fill=b)
        canvas.create_rectangle(x +4*d, y +  d , x + 5*d, y + 2 * d,fill=b)
        canvas.create_rectangle(x +4*d, y   , x + 5*d, y +  d,fill=b)
        canvas.create_rectangle(x  , y + 6 * d , x +  d, y + 7 * d,fill=b)
        canvas.create_rectangle(x +2*d , y + 2 * d , x + 3* d, y + 3 * d,fill=b)

        x = 15 * d

        canvas.create_rectangle(x+2*d, y , x + 3*d, y + d,fill=b)
        canvas.create_rectangle(x + 3*d, y  , x + 4 * d, y + d,fill=b)
        canvas.create_rectangle(x + 4 * d, y, x + 5 * d, y + d, fill=b)
        canvas.create_rectangle(x +d, y + 5 * d , x + 2*d, y + 6 * d,fill=b)
        canvas.create_rectangle(x +d, y + 4 * d , x + 2*d, y + 5 * d,fill=b)
        canvas.create_rectangle(x + d, y + 3 * d, x + 2 * d, y + 4 * d, fill=b)
        canvas.create_rectangle(x +d, y + 2 * d , x +2* d, y + 3 * d,fill=b)
        canvas.create_rectangle(x +d, y +  d , x +2* d, y + 2 * d,fill=b)
        canvas.create_rectangle(x +5*d, y + 5 * d , x + 6*d, y + 6 * d,fill=b)
        canvas.create_rectangle(x +5*d, y + 4 * d , x + 6*d, y + 5 * d,fill=b)
        canvas.create_rectangle(x +5*d, y + 3 * d , x + 6*d, y + 4 * d,fill=b)
        canvas.create_rectangle(x +5*d, y + 2 * d , x +6* d, y + 3 * d,fill=b)
        canvas.create_rectangle(x +5*d, y +  d , x +6* d, y + 2 * d,fill=b)
        canvas.create_rectangle(x+2*d, y +6*d, x + 3*d, y + 7*d,fill=b)
        canvas.create_rectangle(x + 3*d, y +6*d , x + 4 * d, y + 7*d,fill=b)
        canvas.create_rectangle(x + 4 * d, y +6*d , x + 5 * d, y +  7*d,fill=b)

        x = 22 * d




        canvas.create_rectangle(x +4*d, y + 6 * d , x + 5*d, y + 7 * d,fill=b)
        canvas.create_rectangle(x +4*d, y + 5 * d , x + 5*d, y + 6 * d,fill=b)
        canvas.create_rectangle(x +4*d, y + 4 * d , x + 5*d, y + 5 * d,fill=b)
        canvas.create_rectangle(x +4*d, y + 3 * d , x + 5*d, y + 4 * d,fill=b)
        canvas.create_rectangle(x +4*d, y + 2 * d , x + 5*d, y + 3 * d,fill=b)
        canvas.create_rectangle(x +4*d, y +  d , x + 5*d, y + 2 * d,fill=b)
        canvas.create_rectangle(x +4*d, y   , x + 5*d, y +  d,fill=b)
        canvas.create_rectangle(x , y + 6 * d , x +d, y + 7 * d,fill=b)
        canvas.create_rectangle(x , y + 5 * d , x + d, y + 6 * d,fill=b)
        canvas.create_rectangle(x , y + 4 * d , x + d, y + 5 * d,fill=b)
        canvas.create_rectangle(x , y + 3 * d , x + d, y + 4 * d,fill=b)
        canvas.create_rectangle(x , y + 2 * d , x + d, y + 3 * d,fill=b)
        canvas.create_rectangle(x , y +  d , x + d, y + 2 * d,fill=b)
        canvas.create_rectangle(x , y   , x + d, y +  d,fill=b)
        canvas.create_rectangle(x +d, y + 2 * d , x + 2*d, y + 3 * d,fill=b)
        canvas.create_rectangle(x +2*d, y + 3 * d , x + 3*d, y + 4 * d,fill=b)
        canvas.create_rectangle(x +3*d, y + 4 * d , x + 4*d, y + 5 * d,fill=b)
        x = x + dlzka
    y = y + vyska + d
    x = xx


canvas.mainloop()