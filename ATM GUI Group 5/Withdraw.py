from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def land_page():
    a3.destroy()
    import LandingPage
def dep_osit():
    a3.destroy()
    import depo

def ten_click():
    global balance2

    if 10 > balance2:
        messagebox.showerror("ERROR", "Insufficient funds.")
    else:
        balance2 -= 10
        messagebox.showinfo("RECEIPT", f"You Withdrew ${balance2}")


def ten_click():
    global balance2

    if 10 > balance2:
        messagebox.showerror("ERROR", "Insufficient funds.")
    else:
        balance2 -= 10
        messagebox.showinfo("RECEIPT", f"You Withdrew $10m\n Current Balance: ${balance2}")


def twenty_click():
    global balance2

    if 20 > balance2:
        messagebox.showerror("ERROR", "Insufficient funds.")
    else:
        balance -= 20
        messagebox.showinfo("RECEIPT", f"You Withdrew $20\n Current Balance: ${balance2}")


def fifty_click():
    global balance2

    if 50 > balance2:
        messagebox.showerror("ERROR", "Insufficient funds.")
    else:
        balance -= 50
        messagebox.showinfo("RECEIPT", f"You Withdrew $50m\n Current Balance: ${balance2}")


def hundred_click():
    global balance2

    if 100 > balance2:
        messagebox.showerror("ERROR", "Insufficient funds.")
    else:
        balance -= 100
        messagebox.showinfo("RECEIPT", f"You Withdrew $100m\n Current Balance: ${balance2}")
def on_click(event):
    if amount.get()=='Enter Amount':
        amount.delete(0,END)
def off_click(event):
    if amount.get()=='':
        amount.insert(0,'Enter Amount')
def withdraw_amount():
    global balance2
    try:
        am = float(amount.get())
        if am > balance2:
            messagebox.showerror("ERROR", "Insufficient funds.")
        else:
            balance2 -= am
            messagebox.showinfo("RECEIPT", f"You Withdrew ${am}\n Current Balance: ${balance2}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")


balance2 = 0
a3 = Tk()
a3.title('WITHDRAW')
a3.iconbitmap('Atm.ico')
bg = ImageTk.PhotoImage(file='real.png')
bgLab = Label(a3, image=bg)
bgLab.grid(row=0, column=0)
a3.resizable(0,0)
depbuttt=ImageTk.PhotoImage(file='depbut.png')

amount = Entry(a3, width=15,font=('Sans Serif',10,'bold'),bg='gray80',bd=0,fg='black', justify=CENTER)
amount.place(x=70, y=480)
amount.insert(0,'Enter Amount')
amount.bind('<FocusIn>',on_click)
amount.bind('<FocusOut>',off_click)

wdrawbut = Button(a3, text="ENTER", width=10, font=('Sans Serif', 10, 'bold'), bg='#43ee3d', fg='black', command=withdraw_amount)
wdrawbut.place(x=230, y=460)

ten_button = Button(a3, text="$10", width=6, font=('Sans Serif', 8, 'bold'), bg='#43ee3d', fg='black', command=ten_click)
ten_button.place(x=68, y=405)

twenty_button = Button(a3, text="$20", width=6, font=('Sans Serif', 8, 'bold'), bg='#43ee3d', fg='black', command=twenty_click)
twenty_button.place(x=130, y=405)

fifty_button = Button(a3, text="$50", width=6, font=('Sans Serif', 8, 'bold'), bg='#43ee3d', fg='black', command=fifty_click)
fifty_button.place(x=68, y=435)

hundred_button = Button(a3, text="$100", width=6, font=('Sans Serif', 8, 'bold'), bg='#43ee3d', fg='black', command=hundred_click)
hundred_button.place(x=130, y=435)

dposit=Button(a3, image=depbuttt
          ,bd=0,bg='linen',width=40,height=48, command=dep_osit)
dposit.place(x=180, y=580)

backbutton=Button(a3, text='Back',width=10,font=('MS Reference Sans Serif',16,'bold'),activebackground='green',
                activeforeground='black',bd=3, fg='white', bg='gray44', cursor='hand2', command=land_page)
backbutton.place(x=29,y=40)

a3.mainloop