from cProfile import label
from tkinter import *
import tkinter
from tkinter.ttk import *
from turtle import width


top = tkinter.Tk()
top.title("My Image Editor")
top.geometry('1000x650')
top.configure(bg="#262625")

Brightness = DoubleVar(top, value = 0)
Saturation = DoubleVar(top, value = 0)
Sharpness = DoubleVar(top, value = 0)
Exposure = DoubleVar(top, value = 0)
Contrast = DoubleVar(top, value = 0) 

openB = tkinter.Button(top, text='Open', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri")
openB.grid(row = 0, column = 0, sticky = W, pady = 1, padx = 7, ipadx=5)

saveB = tkinter.Button(top, text='Save', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri")
saveB.grid(row = 0, column = 1, sticky = W, pady = 1, padx = 7, ipadx=5)

Space = Label(top)
Space.grid(row = 1, column = 2, padx=50, pady=1)

CropB = tkinter.Button(top, text='Crop', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri")
CropB.grid(row = 1, column = 0, sticky = W, pady = 1, padx = 7, ipadx=5)

Rotate_LeftB = tkinter.Button(top, text='Rotate Left', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri")
Rotate_LeftB.grid(row = 2, column = 0, sticky = W, pady = 1, padx = 7, ipadx=5)

Rotate_RightB = tkinter.Button(top, text='Rotate Right', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri")
Rotate_RightB.grid(row = 2, column = 1, sticky = W, pady = 1, padx = 7, ipadx=5)

#Brightness
Bscale = Scale(top, variable = Brightness, from_ = -100, to = 100, orient = HORIZONTAL)
Bscale.grid(row = 3, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

BrightnessB = tkinter.Button(top, text='Set Brightness', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
BrightnessB.grid(row = 3, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

#Saturation
Sscale = Scale(top, variable = Saturation, from_ = -100, to = 100)
Sscale.grid(row = 4, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

SaturationB = tkinter.Button(top, text='Set Saturation', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
SaturationB.grid(row = 4, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

#Contrast
Cscale = Scale(top, variable = Contrast, from_ = -100, to = 100)
Cscale.grid(row = 5, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

ContrastB = tkinter.Button(top, text='Set Contrast', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
ContrastB.grid(row = 5, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

#Exposure
Escale = Scale(top, variable = Exposure, from_ = -100, to = 100)
Escale.grid(row = 6, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

ExposureB = tkinter.Button(top, text='Set Exposure', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
ExposureB.grid(row = 6, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

#Sharpness
SHscale = Scale(top, variable = Sharpness, from_ = -100, to = 100)
SHscale.grid(row = 7, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

SharpnessB = tkinter.Button(top, text='Set Sharpness', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
SharpnessB.grid(row = 7, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

#Edge-Detection
EDB = tkinter.Button(top, text='Apply Edge-detection', width=16, background="#545451", foreground="white", borderwidth=2, font="calibri")
EDB.grid(row = 8, column = 0, columnspan=3, sticky = W, pady = 0, padx = 7, ipadx=5)

Area = Canvas( top,  width=600, height=500)
Area.grid(row=1, column=4, rowspan=10)

top.mainloop()
