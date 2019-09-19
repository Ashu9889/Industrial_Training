from tkinter  import *
import random
import time
import threading
num=0
score=0
los=0
def click(e):
    global score,los
    if(e.widget["bg"]=="red"):
        score=score+1
        txt.set(score)
    else:
        los=los+1
        lost.set(los)
        if(los==10):
            lost.set("you lost")

def chngcolor():
    global los
    while (los!=10):
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        btnlist = root.grid_slaves(row=i, column=j)
        btn = btnlist[0]
        btn["bg"] = "red"
        time.sleep(0.5)
        btn["bg"] = "grey"

root=Tk()
root.geometry("400x400")
btn = Button(root, text=str(num), width=9, height=4, bg="grey")
th1=threading.Thread(target=chngcolor)
label1=Label(root,text="Score :")
txt=StringVar()
entry=Entry(root,textvariable=txt)
entry.place(x=160,y=300)
label1.place(x=120,y=300)
label2=Label(root,text="loose :")
lost=StringVar()
entry=Entry(root,textvariable=lost)
entry.place(x=160,y=340)
label2.place(x=120,y=340)
for i in range(4):
    for j in range(4):
        num+=1
        btn=Button(root,text=str(num),width=9,height=4,bg="grey")
        btn.bind("<Button 1>",click)
        btn.grid(row=i,column=j)
th1.start()
root.mainloop()
