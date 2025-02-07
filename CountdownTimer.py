from tkinter import *
from playsound import playsound
import time
import threading


root=Tk()
root.geometry("400x600")
root.resizable(False,False)
root.title("TİMER")
root.config(bg="black")

heading=Label(root,text="Timer",font="arial 30 bold",fg="red",bg="black")
heading.pack(pady=10)

Label(root,text="Current time:",fg="white",bg="black",font=("arial",15,"bold")).place(x=65,y=70)

current_t=Label(root,text="",font=("arial",14,"bold"),fg="white",bg="black")
current_t.place(x=195,y=72)

def clock():
    clock_t=time.strftime("%H:%M:%S %p")
    current_t.config(text=clock_t)
    current_t.after(1000,clock)

clock()


ent1=StringVar()
Entry(root,textvariable=ent1,width=2,font="arial 50",fg="#fff",bg="#000",bd=0).place(x=30,y=155)
ent1.set("00")

ent2=StringVar()
Entry(root,textvariable=ent2,width=2,font="arial 50",fg="#fff",bg="#000",bd=0).place(x=150,y=155)
ent2.set("00")

ent3=StringVar()
Entry(root,textvariable=ent3,width=2,font="arial 50",fg="#fff",bg="#000",bd=0).place(x=270,y=155)
ent3.set("00")

Label(root,text="Hours",font="arial 12",fg="#fff",bg="#000").place(x=105,y=200)
Label(root,text="Min",font="arial 12",fg="#fff",bg="#000").place(x=225,y=200)
Label(root,text="Sec",font="arial 12",fg="#fff",bg="#000").place(x=345,y=200)

#TIMER FUNCTIONALITY
running=False
sound_thread=None

def start():
    global running
    running=True

    times=int(ent1.get())*3600+int(ent2.get())*60+int(ent3.get())

    while times>-1 and running:
        minute,second=(times//60,times%60)
        hour=0
        if minute >60:
            hour,minute=(minute//60,minute%60)
        
        ent3.set(second)
        ent2.set(minute)
        ent1.set(hour)

        root.update()
        time.sleep(1)

        if times==0 and running:
            play_alarm()
            ent1.set("00")
            ent2.set("00")
            ent3.set("00")

        times-=1

def play_alarm():
    global sound_thread
    sound_thread=threading.Thread(target=lambda:playsound("C:\\Users\\uzayv\\Downloads\\jolly-ring-287810.mp3"))
    sound_thread.start()

def stop():
    global running
    running=False


def reset():
    global running
    running = False  # Counter stopped
    ent1.set("00")
    ent2.set("00")
    ent3.set("00")


def brush():
    ent1.set("00")
    ent2.set("02")
    ent3.set("00")

def face():
    ent1.set("00")
    ent2.set("15")
    ent3.set("00")

def eggs():
    ent1.set("00")
    ent2.set("10")
    ent3.set("00")


#rst btn
btn_Rst=Button(root,text="RESET",bg="green",fg="white",width=20,height=1,font="arial 12 bold",command=reset)
btn_Rst.pack(side=BOTTOM,padx=5,pady=13)

btn_Stp=Button(root,text="STOP",bg="blue",fg="white",width=20,height=1,font="arial 12 bold",command=stop)
btn_Stp.pack(side=BOTTOM,padx=5,pady=14)

btn_strT=Button(root,text="START",fg="white",bg="red",font="arial 12 bold",width=20,height=1,command=start)
btn_strT.pack(side=BOTTOM,padx=5,pady=15)




#Tımer presents
image1=PhotoImage(file="C:\\Users\\uzayv\\Downloads\\brush.png")
Btn1=Button(root,image=image1,bg="#000",bd=0,command=brush)
Btn1.place(x=7,y=300)

image2=PhotoImage(file="C:\\Users\\uzayv\\Downloads\\face.png")
Btn2=Button(root,image=image2,bg="#000",bd=0,command=face)
Btn2.place(x=137,y=300)

image3=PhotoImage(file="C:\\Users\\uzayv\\Downloads\\eggs.png")
Btn3=Button(root,image=image3,bg="#000",bd=0,command=eggs)
Btn3.place(x=267,y=300)






root.mainloop()