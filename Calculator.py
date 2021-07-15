# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:09:01 2021

@author: Priyanka Ashra
"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

root=Tk()
root.title("Calculator")
root.geometry("1200x550")
root.config(bg="light yellow")

#Cost Avoidance
Window3=LabelFrame(root, text="Cost Avoidance", bg="light blue", bd=10, relief=GROOVE)
Window3.place(x=800,y=50,height=330,width=330)

#Cost Avoidance
label_Value5=tk.Label(Window3, text="First Quote: ", bg="blue", fg="white", relief=GROOVE)
label_Value5.place(x=10, y=50, height=30, width=120)

#Cost Avoidance
label_Value6=tk.Label(Window3, text="Final Quote: ", bg="blue", fg="white", relief=GROOVE)
label_Value6.place(x=10,y=85, height=30, width=120)
label_Value7=tk.Label(Window3, text="Cost Savings: ", bg="blue", fg="white", relief=GROOVE)
label_Value7.place(x=10,y=120, height=30, width=120)

#Cost Avoidance
Entry_5=tk.Entry(Window3)
Entry_5.place(x=150, y=50, height=30, width=140)
Entry_6=tk.Entry(Window3)
Entry_6.place(x=150, y=85, height=30, width=140)
Entry_7=tk.Entry(Window3)
Entry_7.place(x=150, y=120, height=30, width=140)

#Cost Avoidance
Button5=Button(Window3, text="Clear", command=lambda:button_clear3(), bg="blue", fg="white", relief=GROOVE)
Button5.place(x=30, y=180, height=40, width=80)
Button6=Button(Window3, text="Calculate", command=lambda:input_data3(), bg="blue", fg="white", relief=GROOVE)
Button6.place(x=200, y=180, height=40, width=80)

#Cost Avoidane
Label_Result5=tk.Label(Window3, text="Result: ", justify=LEFT, bg="white", fg="black")
Label_Result5.place(x=25, y=240, height=35, width=100)
Label_Result6=tk.Label(Window3, text=" ", bg="white", fg="black")
Label_Result6.place(x=100, y=240, height=35, width=190)

#Cost Avoidance
def input_data3():
    value5=float(Entry_5.get())
    value6=float(Entry_6.get())
    value7=float(Entry_7.get())
    Result3=(value5-value6-value7)
    Label_Result6['text']=Result3
    
#Cost Avoidance
def button_clear3():
    Entry_5.delete(0, 'end')
    Entry_6.delete(0, 'end')
    Entry_7.delete(0, 'end')
    Label_Result6.config(text="")
    
root.mainloop()













