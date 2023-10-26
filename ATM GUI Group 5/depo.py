from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def land_page():
    a2.destroy()
    import LandingPage
def with_draw():
    a2.destroy()
    import Withdraw
def on_click(event):
    if amount.get()=='Enter Amount':
        amount.delete(0,END)
def off_click(event):
    if amount.get()=='':
        amount.insert(0,'Enter Amount')
def bal():
    global balance1
    messagebox.showinfo('BALANCE',f"You Deposited {balance1}")
def withdraw_amount():
    global balance1
    try:
        am = float(amount.get())
        if am > balance1:
            balance1 += am
            messagebox.showinfo("RECEIPT", f"You Deposited ${balance1}")
            
            
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")

balance1 = 0
a2 = Tk()
a2.title('DEPOSIT')
a2.iconbitmap('Atm.ico')
bg = ImageTk.PhotoImage(file='deposit.png')
bgLab = Label(a2, image=bg)
bgLab.grid(row=0, column=0)
a2.resizable(0,0)
widrawww=ImageTk.PhotoImage(file='wdbut.png')

wdraw=Button(a2, image=widrawww,width=40,height=49
          ,bd=0,bg='linen', command=with_draw)
wdraw.place(x=181, y=592)

amount = Entry(a2, width=15,font=('Sans Serif',10,'bold'),bg='gray80',bd=0,fg='black', justify=CENTER)
amount.place(x=66, y=450)
amount.insert(0,'Enter Amount')
amount.bind('<FocusIn>',on_click)
amount.bind('<FocusOut>',off_click)

depobut = Button(a2, text="DEPOSIT", width=10, font=('Sans Serif', 10, 'bold'), bg='#43ee3d', fg='black', command=withdraw_amount)
depobut.place(x=75, y=480)

backbutton=Button(a2, text='Back',width=10,font=('MS Reference Sans Serif',16,'bold'),activebackground='green',
                activeforeground='black',bd=3, fg='white', bg='gray44', cursor='hand2', command=land_page)
backbutton.place(x=29,y=40)

a2.mainloop