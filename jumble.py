from tkinter import *
import random

words = ('computer','bike','system','marker','mobile','physics','chemistry','maths','python','modak','time','success')
jumbled = ('putcorem','ikbe','tesmys','kamrre','bilome','sicysph','mischeyrt','tsmha','thpyno','akdom','mite','sccessu')

r = random.randint(0,12)

def display():
    global words,jumbled,r
    l1.config(text=jumbled[r])

def reset():
    global words,jumbled,r,lbx
    r = random.randint(0,12)
    l1.config(text=jumbled[r])
    e.delete(0,END)

def check():
    global words,jumbled,r
    lbx = Listbox(root,height=1,width=30,fg='red',bg='pink',font='comicsansms 10 bold')
    lbx.grid(row=5,column=1)

    s1 = s.get()
    if s1==words[r]:
        lbx.insert(1,"!!!CONGRATULATION!!!")
        lbx.insert(2,"YOUR ARE INCORRECT")

    else:
        lbx.insert(1,"YOU ARE INCORRECT")


root = Tk()

root.geometry('400x300+700+100')


l2 = Label(root,text="",font='comicsansms 10 bold')
l2.grid()

l = Label(root,text="JUMBLE WORDS",fg='dark blue',font='comicsansms 15 bold')
l.grid(row=0,column=1)

l1 = Label(root,text="",font='comicsansms 15 bold')
l1.grid(row=2,column=1)

s = StringVar()
e = Entry(root,textvariable=s)
e.grid(row=3,column=1)

b = Button(root,text="CHECK",fg='dark green',bg='light green',font='comicsansms 10 bold',command=check)
b.grid(row=4,column=0)

b1=Button(root,text="NEXT",fg='red',bg='pink',font='comicsansms 10 bold',command=reset)
b1.grid(row=4,column=2)

display()
reset()


root.title("JUMBLE WORDS GAME")
root.mainloop()
    
