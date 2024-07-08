pip install torch

import torch
print(torch.__version__)

pip install scipy

from scipy.io.wavfile import write

from tkinter import *
from tkinter.messagebox import showinfo,showwarning
from tkinter.filedialog import askdirectory
from tkinter import Tk, PhotoImage, Label, Entry, Button, messagebox
import os


#Creating the window for the to-do-list

w=Tk()
w.title("To-Do-List")
w.geometry("500x700")
w.resizable(False,False)

#initializing the task-list
task_l=[]

#creating function to add task to to-do-list
def addt():
    task=t_enter.get()
    t_enter.delete(0,END)

    if task:
        with open("task.txt","a") as tfile:
            tfile.write(f"\n{task}")
        task_l.append(task)
        l.insert(END,task)
        
        
#function to delete task from the to-do-list
def delete_t():
    global task_l
    task=str(l.get(ANCHOR))
    if task in task_l:
        task_l.remove(task)
        with open("task.txt","w") as tfile:
            for task in task_l:
                tfile.write(task+"\n")
        
        l.delete(ANCHOR)
            
            
#creating the required function to add task to the to-do-list
def opentask():
    
    try:
        global task_l
        with open("task.txt","r") as tfile:
             tas=tfile.readlines
        
        for task in tas:
            if task !="\n":
                task_l.append(task)
                l.insert(END,task)
    except:
        file=open("task.txt","w")
        file.close()
            
            
# Adding icons and images
img1 = PhotoImage(file="todo1.png")
w.iconphoto(False, img1)

# Creating top of the to-do-list
topimg=PhotoImage(file="top.png")
Label(w,image=topimg).pack()

#adding menu icon in top bar
menu=PhotoImage(file="menu.png")
Label(w, image=menu, bg="#32405b").place(x=25,y=30)

#adding the checklist to the top bar
checkit=PhotoImage(file="todo2.png")
Label(w, image=checkit, bg="#32405b").place(x=425,y=30)

#adding heading to the top bar
head=Label(w,text="ALL YOUR TASKS", font="arial 20 bold",fg="black")
head.place(x=130,y=35)

#main tasks addition
f=Frame(w,width=700,height=50,bg="white")
f.place(x=0,y=180)

#taking task entry
t=StringVar()
t_enter=Entry(f,width=18,font="arial 20",bd=0)
t_enter.place(x=55,y=7)
t_enter.focus()


#adding button to add the tsk
b=Button(f,text="ADD",font="arial 20 bold",width=6,bg="#32405b",fg="black",bd=0,command=addt)
b.place(x=400,y=0)

#adding listbox frame 
f1=Frame(w,bd=3,width=700,height=280,bg="#32405b")
f1.pack(pady=(160,0))

l=Listbox(f1,font=("arial",13),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
l.pack(side=LEFT,fill=BOTH,padx=1)
sc=Scrollbar(f1)
sc.pack(side=RIGHT,fill=BOTH)
l.config(yscrollcommand=sc.set)
sc.config(command=l.yview)

opentask()

#adding the delete button for task completed
d_img=PhotoImage(file="delete1.png")
Button(w,image=d_img,bd=0,command=delete_t).pack(side=BOTTOM,pady=13)


w.mainloop()
