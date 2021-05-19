import turtle as turtle
turtle.bgcolor("black")   # background color of window.
turtle.color("#ff8000")   # pencolor used for drawing.
turtle.speed(0)           # slow motion.
turtle.pensize(3)         # size of pen

turtle.penup()
turtle.goto(0,-130)
turtle.pendown()
# chandrakor code.
turtle.circle(120,-80,45)
turtle.circle(120,160,45)
turtle.circle(119,-80,50)
turtle.circle(119,-80,50)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

# first shapes
turtle.color("#ff8000")
turtle.begin_fill()
turtle.left(80)
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
turtle.goto(0,70)
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