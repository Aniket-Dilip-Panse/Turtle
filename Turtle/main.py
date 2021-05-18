def circle(x,y,color,radius):
    tur.penup()
    tur.speed(0)
    for i in range(40):
        tur.pendown()
        tur.goto(x,y)
        tur.begin_fill()
        tur.color(color)
        tur.end_fill()
        tur.circle(radius)
        tur.left(10)
import turtle as tur
circle(0,0,"pink",100)
tur.bgcolor("black")
tur.penup()
tur.goto(150,-225)
tur.pendown()
tur.write("First-Try",font=('arial',25))
tur.mainloop()