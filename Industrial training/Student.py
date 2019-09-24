from tkinter import *
from tkinter import ttk
from pymysql import *



class  Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="grey",fg="white",bd=10)
        title.pack(side=TOP,fill=X)

        #variables.....................
        self.roll_no=StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.seachby=StringVar()
        self.searchtext=StringVar()



        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_frame.place(x=20,y=100,width=450,height=600)


        m_title=Label(manage_frame,text="Manage Students",bg="crimson",fg="white",font=("",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(manage_frame, text="Roll No", bg="crimson", fg="white", font=("", 20, "bold"))
        lbl_roll.grid(row=1, column=0, padx=20,pady=10,sticky="w")
        entry_roll=Entry(manage_frame,textvariable=self.roll_no, font=("", 15, "bold"),bd=5,relief=GROOVE)
        entry_roll.grid(row=1, column=1, padx=20,pady=10,sticky="w")



        lbl_name = Label(manage_frame, text="Name", bg="crimson", fg="white", font=("", 20, "bold"))
        lbl_name.grid(row=2, column=0, padx=20,pady=10,sticky="w")
        entry_name=Entry(manage_frame,textvariable=self.name, font=("", 15, "bold"),bd=5,relief=GROOVE)
        entry_name.grid(row=2, column=1, padx=20,pady=10,sticky="w")



        lbl_email = Label(manage_frame, text="Email", bg="crimson", fg="white", font=("", 20, "bold"))
        lbl_email.grid(row=3, column=0, padx=20,pady=10,sticky="w")
        entry_email=Entry(manage_frame,textvariable=self.email, font=("", 15, "bold"),bd=5,relief=GROOVE)
        entry_email.grid(row=3, column=1, padx=20,pady=10,sticky="w")


        lbl_gender = Label(manage_frame, text="Gender", bg="crimson", fg="white", font=("", 20, "bold"))
        lbl_gender.grid(row=4, column=0, padx=20,pady=10,sticky="w")
        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender,font=("", 13, "bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10,sticky="w")

        lbl_contact = Label(manage_frame, text="Contact", bg="crimson", fg="white", font=("", 20, "bold"))
        lbl_contact.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        entry_contact = Entry(manage_frame,textvariable=self.contact, font=("", 15, "bold"), bd=5, relief=GROOVE)
        entry_contact.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        lbl_dob = Label(manage_frame, text="D.O.B", bg="crimson", fg="white", font=("", 20, "bold"))
        lbl_dob.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        entry_dob = Entry(manage_frame,textvariable=self.dob, font=("", 15, "bold"), bd=5, relief=GROOVE)
        entry_dob.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        lbl_address = Label(manage_frame, text="Address", bg="crimson", fg="white", font=("", 20, "bold"))
        lbl_address.grid(row=7, column=0, padx=20, pady=10, sticky="w")
        self.entry_address=Text(manage_frame,width=25,height=4)
        self.entry_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        btn_frame = Frame(manage_frame, bd=1, relief=RIDGE, bg="crimson")
        btn_frame.place(x=15, y=530, width=420)

        addbtn=Button(btn_frame,command=self.add_student,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame,command=self.update, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame,command=self.delete, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame,command=self.clear, text="Clear", width=10).grid(row=0, column=3, padx=10, pady=10)

        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frame.place(x=500, y=100, width=820, height=560)


        lbl_search = Label(detail_frame, text="Search By", bg="crimson", fg="white", font=("", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        combo_search = ttk.Combobox(detail_frame,textvariable=self.seachby,width=10, font=("", 13, "bold"), state="readonly")
        combo_search['values'] = ("roll_no", "name", "contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        entry_search = Entry(detail_frame,textvariable=self.searchtext,width=15, font=("", 10, "bold"), bd=1, relief=GROOVE)
        entry_search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        searchbtn = Button(detail_frame,command=self.search, text="Search", width=10).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(detail_frame,command=self.fetch_data, text="Show All", width=10).grid(row=0, column=4, padx=10, pady=10)

        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="crimson")
        table_frame.place(x=10,y=70,width=760,height=480)
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.Student_table=ttk.Treeview(table_frame,column=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll",text="Roll No.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("DOB", text="DOB")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show']="headings"
        # self.Student_table.column("Roll",width=100)
        # self.Student_table.column("Name",width=100)
        # self.Student_table.column("Email", width=100)
        # self.Student_table.column("Gender", width=100)
        # self.Student_table.column("Contact",width=100)
        # self.Student_table.column("DOB", width=100)
        # self.Student_table.column("Address", width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_student(self):
        db = connect("localhost", "root", "1234", "mydatabase")
        cursor = db.cursor()

        cursor.execute("INSERT INTO STUDENTS VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no.get(),self.name.get(),self.email.get(),self.gender.get(),
                                                                                   self.contact.get(),self.dob.get(),self.entry_address.get('1.0',END)))
        db.commit()

        self.fetch_data()
        db.close()

    def fetch_data(self):
        db = connect("localhost", "root", "1234", "mydatabase")
        cursor = db.cursor()

        cursor.execute("select * from students")
        result=cursor.fetchall()
        if len(result)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in result:
                self.Student_table.insert('',END,values=row)
            db.commit()
        self.clear()
        db.close()

    def clear(self):
        self.roll_no.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.dob.set("")
        self.entry_address.delete("1.0",END)
    def get_cursor(self,temp):
        cu=self.Student_table.focus()
        content=self.Student_table.item(cu)
        row=content['values']
        self.roll_no.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[4])
        self.dob.set(row[5])
        self.entry_address.delete("1.0",END)
        self.entry_address.insert(END,row[6])

    def update(self):
        db = connect("localhost", "root", "1234", "mydatabase")
        cursor = db.cursor()

        cursor.execute("UPDATE STUDENTS SET name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",
                       ( self.name.get(), self.email.get(), self.gender.get(),
                        self.contact.get(), self.dob.get(), self.entry_address.get('1.0', END),self.roll_no.get()))
        db.commit()

        self.fetch_data()
        db.close()
    def delete(self):
        db = connect("localhost", "root", "1234", "mydatabase")
        cursor = db.cursor()
        cursor.execute("delete from students where roll_no=%s",self.roll_no.get())
        db.commit()
        db.close()
        self.fetch_data()
        self.clear()

    def search(self):
        db = connect("localhost", "root", "1234", "mydatabase")
        cursor = db.cursor()

        cursor.execute("select * from students where "+str(self.seachby.get())+" LIKE '%"+str(self.searchtext.get())+"%'")
        result=cursor.fetchall()
        if len(result)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in result:
                self.Student_table.insert('',END,values=row)
            db.commit()
        db.close()


root=Tk()
ob=Student(root)
root.mainloop()
