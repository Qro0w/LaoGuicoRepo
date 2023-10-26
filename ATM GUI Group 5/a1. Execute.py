from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def sign_up():
    a1.destroy()
    import SignUpWindow
    
def log_data():
    if cardnum.get() == '05-2324-006118' and pin.get() ==  '1234':
        messagebox.showinfo('Login Successful!','Welcome To LUX Bank')
        a1.destroy()
        import LandingPage
    else:
         messagebox.showerror('Login Error','Please Login Again')
a1 = Tk()
a1.title('LUX')
a1.resizable(0,0)
a1.iconbitmap('Atm.ico')
bg=ImageTk.PhotoImage(file='Login.jpg')
bgLab=Label(a1, image=bg)
bgLab.grid(row=0, column=0)

cardnum=Entry(a1, width=17,font=('Times New Roman',20,'bold')
          ,bg='gray77',bd=0,fg='gray10', justify=CENTER)
cardnum.place(x=88, y=540)

pin=Entry(a1, width=17,font=('Times New Roman',20,'bold')
          ,bg='gray77',bd=0,fg='gray10', justify=CENTER, show='*')
pin.place(x=88, y=623)

signupbut=Button(a1, text='Sign Up!',bd=0,bg='white',fg='green',activebackground='white',
               activeforeground='gray77',font=('Roboto', 10, 'bold')
               , command=sign_up)
signupbut.place(x=173,y=800)

loginbut=Button(a1, text='Login',width=17,font=('Open Sans',16,'bold'),activebackground='green',
                activeforeground='black',bd=5, fg='white', bg='gray17', cursor='hand2', command=log_data)
loginbut.place(x=88,y=690)

a1.mainloop()