from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
    
def with_draw():
    a1.destroy()
    import Withdraw
    
def depo_sit():
    a1.destroy()
    import depo
def balast():
    balmain=0
    messagebox.showinfo('CURRENT',balmain)
a1 = Tk()
a1.title('LUX')
a1.resizable(0,0)
a1.iconbitmap('Atm.ico')
bg=ImageTk.PhotoImage(file='LandingPage.png')
bgLab=Label(a1, image=bg)
bgLab.grid(row=0, column=0)
depbuttt=ImageTk.PhotoImage(file='depbut.png')
widrawww=ImageTk.PhotoImage(file='wdbut.png')

wdraw=Button(a1, image=widrawww,width=40,height=49
          ,bd=0,bg='linen', command=with_draw)
wdraw.place(x=78, y=590)

dposit=Button(a1, image=depbuttt,width=40,height=48
          ,bd=0,bg='linen', command=depo_sit)
dposit.place(x=303, y=590)

bal_button=Button(a1, text='Check Balance',bd=0,bg='#07d34b',fg='black',command=balast)
bal_button.place(x=77,y=517)


        
a1.mainloop()
        