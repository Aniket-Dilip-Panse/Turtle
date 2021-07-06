from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image,ImageTk


def showimage():
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='select image file',filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),(" ALL file","*.*")))

    img=Image.open(fln)
    img.thumbnail((350,350))
    img=ImageTk.PhotoImage(img)

    lbl.configure(image=img)  #imp line
    lbl.image=img     # imp line
root=Tk()

frm =Frame(root)
frm.pack(side=BOTTOM,padx=15,pady=15)


lbl=Label(root)
lbl.pack()

btn=Button(frm,text='browse image',command=showimage,padx=20)
btn.pack(side=tk.LEFT)

btn2=Button(frm,text='exit',command=lambda:exit(),padx=20)
btn2.pack(side=tk.LEFT,padx=10)

root.title('image browser')
root.geometry('300x350')
root.mainloop()