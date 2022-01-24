from cProfile import label
from tkinter import *
import tkinter
from tkinter.ttk import *
from turtle import width

top = tkinter.Tk()
top.title("My Image Editor")
top.geometry('850x650')
top.configure(bg="#262625")

openB = tkinter.Button(top, text='Open', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri")
openB.grid(row = 0, column = 0, sticky = W, pady = 10, padx = 7, ipadx=5)


saveB = tkinter.Button(top, text='Save', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri")
saveB.grid(row = 0, column = 1, sticky = W, pady = 4, padx = 7, ipadx=5)

Area = Canvas( top,  width=600, height=500 )
Area.grid(row=1, column=4, rowspan=10)

top.mainloop()