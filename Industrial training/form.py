import Signup
from pymysql import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk



db=connect("localhost","root","1234","mydatabase")
cursor=db.cursor()

class login_system:
            def __init__(self,root):
                self.root=root
                self.root.title("Login System")
                self.root.geometry("1350x700+0+0")
                #for images.....................
                self.bg_icon=ImageTk.PhotoImage(file=r"C:\Users\Ashutosh\PycharmProjects\untitled\Industrial training\img_login.jpg")
                self.user_icon=PhotoImage(file=r"C:\Users\Ashutosh\PycharmProjects\untitled\Industrial training\man-user.png")
                self.pass_icon =PhotoImage(file=r"C:\Users\Ashutosh\PycharmProjects\untitled\Industrial training\password.png")
                self.logo_icon = PhotoImage(file=r"C:\Users\Ashutosh\PycharmProjects\untitled\Industrial training\logo.png")
                #variables for entry.............
                self.username=StringVar()
                self.password=StringVar()
                bg_lb1 = Label(self.root, image=self.bg_icon).pack()

                #login frame......................
                Login_Frame=Frame(self.root,bg="white")

                Login_Frame.place(x=510,y=150,)
                title = Label(Login_Frame, text="Login System", font=("Industry Inc Detail Fill", 40, "bold"),bg="white", fg="gray", bd=0, relief=GROOVE)
                title.grid(row=0,columnspan=2)

                logo1lbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=1,columnspan=2,pady=20)
                labeluser=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("Industry Inc Detail Fill",20,"bold"),bg="white")
                labeluser.grid(row=2,column=0,padx=20,pady=10)
                user_entry=Entry(Login_Frame,bd=5,textvariable=self.username,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
                labelpass = Label(Login_Frame, text="Password", image=self.pass_icon,compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="white")
                labelpass.grid(row=3,column=0,padx=20,pady=10)
                pass_entry = Entry(Login_Frame, bd=5,textvariable=self.password, relief=GROOVE, font=("", 15)).grid(row=3, column=1, padx=20)
                btn_login=Button(Login_Frame,command=self.login,text="Login",width=10,font=("Industry Inc Detail Fill", 20, "bold"),bg="skyblue",fg="white").grid(row=4,column=1,pady=10)
                btn_signup = Button(Login_Frame, command=self.new, text="SignUp", width=10,font=("Industry Inc Detail Fill", 20, "bold"), bg="skyblue", fg="white").grid(row=4,columnspan=1,pady=10)

            def new(self):
                 self.root.withdraw()
                 self.newwindow=Toplevel()
                 ob=Signup.Signup_system(self.newwindow,self.root)





            def login(self):
                sql="SELECT * FROM LOGIN \
                     WHERE FIRST_NAME ='%s' AND PASSWORD ='%s'"%(self.username.get(),self.password.get())
                cursor.execute(sql)
                result=cursor.fetchall()

                # if self.username.get()=="" or self.password.get()=="":
                #     messagebox.showerror("Error","All Fields are required!!")
                if result:
                    messagebox.showinfo("Succesfull",f"Welcome {self.username.get()}")
                    self.username.set("")
                    self.password.set("")
                    db.close()
                elif self.username.get()=="" or self.password.get()=="":
                    messagebox.showerror("Error","ALL FIELDS ARE MANDATRORY")
                    self.username.set("")
                    self.password.set("")
                else:
                    messagebox.showerror("Error","Invalid Username or Password!")
                    self.username.set("")
                    self.password.set("")


root=Tk()
obj=login_system(root)
root.mainloop()



