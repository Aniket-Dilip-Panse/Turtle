# This is important.
import turtle as tur
import random
tur.speed(0)
list1=["red","blue","orange","cyan","violet","purple"]
tur.bgcolor("tomato")
for i in range(200):
    tur.color(random.choice(list1)) # pick up random color.
    tur.pensize(i/10+1) #increase pensize as we move ahead
    tur.fd(i)   # move forward according to size
    tur.right(59) #turn left
tur.mainloop()