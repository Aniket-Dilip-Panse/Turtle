from tkinter import *
root=Tk()
root.title('even or odd')
root.geometry('570x150')

def even_or_odd(): 
    n=int(ent1.get())
    if n==0:
        result=Label(root,text='entered zero not even nor odd').grid(row=3,column=1,columnspan=2)
    elif  n%-2==0:
        result=Label(root,text='entered even number').grid(row=3,column=1,columnspan=2)
    elif n%-2!=0:
        result=Label(root,text='entered odd number').grid(row=3,column=1,columnspan=2)
    elif n==str(eval('')):
        result=Label(root,text='entered invalid number').grid(row=3,column=1,columnspan=2)
        
def clear():
    ent1.delete(0,END)


lab1=Label(root,text='Checking Even or Odd',font=('arial,30,bold'),padx=100)
lab1.grid(row=0,column=0,columnspan=3)

lab2=Label(root,text='Enter Number:',font=('arial,30,bold'))
lab2.grid(row=1,column=0)

ent1=Entry(root,borderwidth=5,bg='powderblue',width=60)
ent1.grid(row=1,column=1,columnspan=3)


btn=Button(root,text='check number',width=15,borderwidth=3,command=even_or_odd)
btn.grid(row=2,column=1)

btnclear=Button(root,text='clear',width=15,borderwidth=3,command=clear)
btnclear.grid(row=2,column=2)

root.mainloop()
