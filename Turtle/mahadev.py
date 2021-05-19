import turtle as turtle
turtle.bgcolor("black")   # background color of window.
turtle.color("#ff8000")   # pencolor used for drawing.
turtle.speed(1)           # slow motion.
turtle.pensize(3)         # size of pen

turtle.penup()
turtle.goto(100,-130)
turtle.pendown()
# chandrakor code.
turtle.begin_fill()
turtle.color("#ff8000")
turtle.right(90)
turtle.circle(-100,180)
turtle.up()
turtle.fd(10)
turtle.down()
turtle.circle(-100,-180)
turtle.end_fill()

turtle.penup()
turtle.goto(0,-50)
turtle.pendown()

# first shapes
turtle.color("#ff8000")
turtle.begin_fill()
turtle.left(90)
turtle.fd(100)
turtle.circle(25,180)
turtle.fd(200)
turtle.circle(25,180)
turtle.fd(100)
turtle.end_fill()
turtle.color("white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(0,30)
turtle.pendown()

# second shapes
turtle.color("#ff8000")
turtle.begin_fill()
turtle.fd(100)
turtle.circle(25,180)
turtle.fd(200)
turtle.circle(25,180)
turtle.fd(100)
turtle.end_fill()
turtle.color("white")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(150,-225)
turtle.pendown()
turtle.write("mera bhola hai bhandari",font=('arial',25))

turtle.hideturtle()
turtle.mainloop()

