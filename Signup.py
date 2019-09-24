from pymysql import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

db=connect("localhost","root","1234","mydatabase")
cursor=db.cursor()

class Signup_system:
            def __init__(self,root,oldmaster):
                self.root=root
                self.root.title("SignUp")
                self.root.geometry("1350x700+0+0")
                #for images.....................
                self.bg_icon=ImageTk.PhotoImage(file=r"C:\Users\Ashutosh\PycharmProjects\untitled\Industrial training\img_login.jpg")
                self.user_icon=PhotoImage(file=r"C:\Users\Ashutosh\PycharmProjects\untitled\Industrial training\man-user.png")
                self.pass_icon =PhotoImage(file=r"C:\Users\Ashutosh\PycharmProjects\untitled\Industrial training\password.png")
                self.logo_icon = PhotoImage(file=r"C:\Users\Ashutosh\PycharmProjects\untitled\Industrial training\logo.png")
                #variables for entry.............
                self.firstname=StringVar()
                self.lastname=StringVar()
                self.age=IntVar()
                self.sex=StringVar()
                self.password=StringVar()
                bg_lb1 = Label(self.root, image=self.bg_icon).pack()

                #login frame......................
                Login_Frame=Frame(self.root,bg="white")

                Login_Frame.place(x=510,y=60,)
                title = Label(Login_Frame, text="SignUp", font=("Industry Inc Detail Fill", 40, "bold"),bg="white", fg="gray", bd=0, relief=GROOVE)
                title.grid(row=0,columnspan=2)

                logo1lbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=1,columnspan=2,pady=20)
                label_first=Label(Login_Frame,text="First name",image=self.user_icon,compound=LEFT,font=("Industry Inc Detail Fill",20,"bold"),bg="white")
                label_first.grid(row=2,column=0,padx=20,pady=10)
                first_entry = Entry(Login_Frame, bd=5, textvariable=self.firstname, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)
                label_last = Label(Login_Frame, text="Last name", image=self.user_icon, compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="white")
                label_last.grid(row=3, column=0, padx=20, pady=10)
                last_entry=Entry(Login_Frame,bd=5,textvariable=self.lastname,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=20)
                labelpass = Label(Login_Frame, text="Password", image=self.pass_icon,compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="white")
                labelpass.grid(row=6,column=0,padx=20,pady=10)
                label_age = Label(Login_Frame, text="Age", image=self.user_icon, compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="white")
                label_age.grid(row=5, column=0, padx=20, pady=10)
                age_entry= Entry(Login_Frame, bd=5, textvariable=self.age, relief=GROOVE, font=("", 15)).grid(row=5, column=1, padx=20)
                pass_entry = Entry(Login_Frame,show="*", bd=5,textvariable=self.password, relief=GROOVE, font=("", 15)).grid(row=6, column=1, padx=20)
                label_sex = Label(Login_Frame, text="Sex", image=self.user_icon, compound=LEFT,font=("Industry Inc Detail Fill", 20, "bold"), bg="white")
                label_sex.grid(row=4, column=0, padx=20, pady=10)
                sex_entry= Entry(Login_Frame, bd=5, textvariable=self.sex, relief=GROOVE, font=("", 15)).grid(row=4, column=1, padx=20)
                btn_signup=Button(Login_Frame,command=lambda:self.signup(oldmaster),text="SignUp",width=15,font=("Industry Inc Detail Fill", 20, "bold"),bg="skyblue",fg="white").grid(row=7,column=1,pady=10)


            def signup(self,oldmaster):
                if self.firstname.get()=="" or self.lastname.get()=="" or self.sex.get()==""or self.age.get()=="" or self.password.get()=="":
                    messagebox.showerror("Error","All Fields Are Mandatory")
                else:
                    sql = "INSERT INTO LOGIN(FIRST_NAME, \
                                      LAST_NAME, AGE, SEX, PASSWORD) \
                                      VALUES ('%s','%s','%d','%s','%s' )" % \
                          (self.firstname.get(), self.lastname.get(),self.age.get(),self.sex.get(),self.password.get())
                    try:
                        # Execute the SQL command
                        cursor.execute(sql)
                        # Commit your changes in the database
                        db.commit()
                        messagebox.showinfo("Successfull","You are SignedUp Please Login")
                    except:
                        # Rollback in case there is any error
                        db.rollback()
                        db.close()
                    oldmaster.deiconify()
                    self.root.destroy()

if __name__=="__main__":
    root = Tk()
    obj = Signup_system(root)
    root.mainloop()





