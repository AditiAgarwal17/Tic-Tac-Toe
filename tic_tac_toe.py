from tkinter import *
from PIL import Image,ImageTk
from tkinter.messagebox import showinfo
root=Tk()
root.title("TIC TAC TOE!")
count = 1
root.geometry("240x400")
root.resizable(0,0)

def disable_all():
    b1.config(state='disable')
    b2.config(state='disable')
    b3.config(state='disable')
    b4.config(state='disable')
    b5.config(state='disable')
    b6.config(state='disable')
    b7.config(state='disable')
    b8.config(state='disable')
    b9.config(state='disable')

def enable_all():
        b1.config(state='active')
        b2.config(state='active')
        b3.config(state='active')
        b4.config(state='active')
        b5.config(state='active')
        b6.config(state='active')
        b7.config(state='active')
        b8.config(state='active')
        b9.config(state='active')
def check_win():
    global winner
    winner=False
    p1="X"
    p2="O"

    if((b1["text"] == b2["text"] == b3["text"] == p1)
     or (b4["text"] == b5["text"] == b6["text"] == p1)
     or (b7["text"] == b8["text"] == b9["text"] == p1)
     or (b1["text"] == b4["text"] == b7["text"] == p1)
     or (b2["text"] == b5["text"] == b8["text"] == p1)
     or (b3["text"] == b6["text"] == b9["text"] == p1)
     or (b1["text"] == b5["text"] == b9["text"] == p1)
     or (b3["text"] == b5["text"] == b7["text"] == p1)):
        showinfo("Result", "Player1 wins")
        winner = True
        disable_all()

    if ((b1["text"] == b2["text"] == b3["text"] == p2)
    or (b4["text"] == b5["text"] == b6["text"] == p2)
    or (b7["text"] == b8["text"] == b9["text"] == p2)
    or (b1["text"] == b4["text"] == b7["text"] == p2)
    or (b2["text"] == b5["text"] == b8["text"] == p2)
    or (b3["text"] == b6["text"] == b9["text"] == p2)
    or (b1["text"] == b5["text"] == b9["text"] == p2)
    or (b3["text"] == b5["text"] == b7["text"] == p2)):
            showinfo("Result", "Player2 wins")
            winner=True
            disable_all()
def b_click(b):
    global count
    global winner
    if (b["text"] == " " and count%2!=0):
        b["text"] = 'X'
        b.config(state="disable")
        count = count + 1
        check_win()

    elif (b["text"] == " " and count%2==0):
        b['text'] = 'O'
        b.config(state="disable")
        count = count + 1
        check_win()

    if count==10 and winner==False:
        showinfo('TIC TAC TOE!', 'It is a TIE!')

def restart():
    global count
    b1["text"] = b2["text"] = b3["text"] =b4["text"] = b5["text"] = b6["text"] =b7["text"] = b8["text"] = b9["text"] =" "
    enable_all()
    count=1



b1=Button(root, text=" ", height=6, width=10,command=lambda : b_click(b1))
b1.grid(row=0, column=0)
b2=Button(root, text=" ",height=6, width=10,command=lambda : b_click(b2))
b2.grid(row=0, column=1)
b3=Button(root, text=" ",height=6, width=10,command=lambda : b_click(b3))
b3.grid(row=0, column=2)
b4=Button(root, text=" ", height=6, width=10,command=lambda : b_click(b4))
b4.grid(row=1, column=0)
b5=Button(root, text=" ",height=6, width=10,command=lambda : b_click(b5))
b5.grid(row=1, column=1)
b6=Button(root, text=" ",height=6, width=10,command=lambda : b_click(b6))
b6.grid(row=1, column=2)
b7=Button(root, text=" ",height=6, width=10,command=lambda : b_click(b7))
b7.grid(row=2, column=0)
b8=Button(root, text=" ",height=6, width=10,command=lambda : b_click(b8))
b8.grid(row=2, column=1)
b9=Button(root, text=" ",height=6, width=10,command=lambda : b_click(b9))
b9.grid(row=2, column=2)

start=Button(root, text="Player1='X'\n Player2='O'!",font=("Arial", 10), bg="black", fg="white")
start.grid(row=3, column=0,columnspan=3,pady=5)
restart=Button(root, text="Restart Game!!",font=("Arial", 10), bg="black", fg="white",command=restart)
restart.grid(row=4, column=0,columnspan=3,pady=5)




root.mainloop()

