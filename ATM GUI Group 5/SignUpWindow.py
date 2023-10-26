from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def land_page():
    a2.destroy()
    import LandingPage

def kill():
    Name.delete(0,END)
    Email.delete(0,END)
    PinCode.delete(0,END)
    dateOB.delete(0,END)

def con_data():
    if Email.get()=='' or PinCode.get()=='' or dateOB.get()=='' or Name.get()=='':
        messagebox.showerror('Error', 'Fields Are Empty!')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root',password='Nazonokanojox123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Issues With Database, Please Retry')
            return
        try:
            query='create database group5'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
        except:
            mycursor.execute('use group5')
            
        query='insert into usergroup(name,email,pin,date) values(%s,%s,%s,%s)'
        mycursor.execute(query,(Name.get(),Email.get(),PinCode.get(),dateOB.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Congratulations!','Sign Up Sucessful!')
        kill()
    
def login_window():
    a2.destroy()
    import LoginWindow
a2 = Tk()
a2.title('LUX') 
a2.resizable(0,0)
a2.iconbitmap('Atm.ico')
bg2=ImageTk.PhotoImage(file='SignUp.jpg')
bgLab2=Label(a2, image=bg2)
bgLab2.grid(row=0, column=0)

Name=Entry(a2, width=27,font=('Times New Roman',14)
          ,bg='gray83',bd=0,fg='black', justify=CENTER)
Name.place(x=88, y=378)

Email=Entry(a2, width=24,font=('Times New Roman',15)
          ,bg='gray83',bd=0,fg='black', justify=CENTER)
Email.place(x=88, y=476)

PinCode=Entry(a2, width=17,font=('Times New Roman',20)
          ,bg='gray83',bd=0,fg='black', justify=CENTER,show='*')
PinCode.place(x=88, y=564)

dateOB=Entry(a2, width=17,font=('Times New Roman',20)
          ,bg='gray83',bd=0,fg='black', justify=CENTER)
dateOB.place(x=88, y=659)

signupbut=Button(a2, text='Sign Up',width=17,font=('Open Sans',16,'bold'),activebackground='green',
                activeforeground='black',bd=5, fg='white', bg='gray17', cursor='hand2', command=con_data)
signupbut.place(x=95,y=732)

loginhere=Button(a2, text='Log In Here', bd=0,bg='white', fg='green', cursor='hand2',
                 activeforeground='gray83', activebackground='white',font=('Open Sans',9)
                 ,command=login_window)
loginhere.place(x=238,y=296)
backbutton=Button(a2, text='Back',width=10,font=('MS Reference Sans Serif',16,'bold'),activebackground='green',
                activeforeground='black',bd=3, fg='white', bg='gray44', cursor='hand2', command=land_page)
backbutton.place(x=29,y=40)

a2.mainloop()