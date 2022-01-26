from cProfile import label
from tkinter import *
import tkinter
import tkinter.filedialog 
from tkinter.ttk import *
from PIL import Image, ImageTk,ImageChops,ImageOps
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)

bc=2
ivcc=2

def open_file():
    global img1,realimg,rs
    top.img1=tkinter.filedialog.askopenfilename(filetypes=( ("jpg files", "*.jpg"), ("png files", "*.png"),("jpeg files", "*.jpeg")))
    realimg=Image.open(top.img1)
    rs=realimg.resize((1030,580))
    global tki
    tki=ImageTk.PhotoImage(rs)
    global yechap
    yechap=Label(Area,image=tki).place(x=1,y=0)



def fi():
   
        global rs
        rs=rs.transpose(Image.FLIP_LEFT_RIGHT)
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(Area,image=hi).place(x=1,y=0)
    
 

def vi():
    
        global rs
        rs=rs.transpose(Image.FLIP_TOP_BOTTOM)
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(Area,image=hi).place(x=1,y=0)
     

def rl():
        global rs
        rs=rs.transpose(Image.ROTATE_90)
        global hi
        rs=rs.resize((1030,580))
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(Area,image=hi).place(x=1,y=0)
      
def rr():
        global rs
        rs=rs.transpose(Image.ROTATE_270)
        global hi
        rs=rs.resize((1030,580))
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(Area,image=hi).place(x=1,y=0)

def bnw():
        global bc
        if bc%2==0:
                bc=3
                global rs 
                global bcha
                bcha=rs
                bcha=bcha.convert("L")
                global hi
                hi=ImageTk.PhotoImage(bcha)
                yechap=Label(Area,image=hi).place(x=1,y=0)
        else:
                hi=ImageTk.PhotoImage(rs)
                yechap=Label(Area,image=hi).place(x=1,y=0)
                bc=2
def ic():
        global rs
        pixels = rs.load()

        for i in range(rs.size[0]):
                for j in range(rs.size[1]):
                        x,y,z = pixels[i,j][0],pixels[i,j][1],pixels[i,j][2]
                        x,y,z = abs(x-255), abs(y-255), abs(z-255)
                        pixels[i,j] = (x,y,z)
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(Area,image=hi).place(x=1,y=0)
    
def saves():
        global rs
        rs= rs.save("save1.jpg")
        
def crops():
        global rs
        rs = rs.crop((1,2,300,300))
        rs=rs.resize((1030, 580))
        global hi
        hi=ImageTk.PhotoImage(rs)
        yechap=Label(Area,image=hi).place(x=1,y=0)

top = tkinter.Tk()
top.title("My Image Editor")
top.geometry('1300x620')
top.configure(bg="#262625")

Brightness = DoubleVar(top, value = 0)
Saturation = DoubleVar(top, value = 0)
Sharpness = DoubleVar(top, value = 0)
Exposure = DoubleVar(top, value = 0)
Contrast = DoubleVar(top, value = 0) 

Space = Label(top, background ="#262625")
Space.grid(row = 0, column = 0)

openB = tkinter.Button(top, text='Open', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri", command=open_file)
openB.grid(row = 1, column = 0, sticky = W, pady = 8, padx = 7, ipadx=5)

saveB = tkinter.Button(top, text='Save', width=9, background="#545451", foreground="white", borderwidth=2, font="calibri", command=saves)
saveB.grid(row = 1, column = 1, sticky = W, pady = 8, padx = 7, ipadx=5)

CropB = tkinter.Button(top, text='Crop', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri", command=crops)
CropB.grid(row = 2, column = 0, sticky = W, pady = 1, padx = 7, ipadx=5)

Rotate_LeftB = tkinter.Button(top, text='Rotate Left', width=8, background="#545451", foreground="white", borderwidth=2, font="calibri", command=rl)
Rotate_LeftB.grid(row = 3, column = 0, sticky = W, pady = 1, padx = 7, ipadx=5)

Rotate_RightB = tkinter.Button(top, text='Rotate Right', width=9, background="#545451", foreground="white", borderwidth=2, font="calibri", command=rr)
Rotate_RightB.grid(row = 3, column = 1, sticky = W, pady = 1, padx = 5, ipadx=5)

VflipB = tkinter.Button(top, text='Verticle flip', width=9, background="#545451", foreground="white", borderwidth=2, font="calibri", command=vi)
VflipB.grid(row = 4, column = 0, sticky = W, pady = 1, padx = 7, ipadx=5)

HflipB = tkinter.Button(top, text='Horizontal flip', width=10, background="#545451", foreground="white", borderwidth=2, font="calibri", command=fi)
HflipB.grid(row = 4, column = 1, sticky = W, pady = 1, padx = 5, ipadx=5)

BnWB = tkinter.Button(top, text='Black&White', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri", command=bnw)
BnWB.grid(row = 5, column = 0, sticky = W, pady = 1, padx = 7, ipadx=5)

InCB = tkinter.Button(top, text='Invert colours', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri", command=ic)
InCB.grid(row = 6, column = 0, sticky = W, pady = 1, padx = 7, ipadx=5)

Area = Canvas( top,  width=1030, height=580)
Area.grid(row=1, column=4, rowspan=10)

   




#Brightness
# Bscale = Scale(top, variable = Brightness, from_ = -100, to = 100, orient = HORIZONTAL)
# Bscale.grid(row = 4, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

# BrightnessB = tkinter.Button(top, text='Set Brightness', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
# BrightnessB.grid(row = 4, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

# #Saturation
# Sscale = Scale(top, variable = Saturation, from_ = -100, to = 100)
# Sscale.grid(row = 5, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

# SaturationB = tkinter.Button(top, text='Set Saturation', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
# SaturationB.grid(row = 5, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

# #Contrast
# Cscale = Scale(top, variable = Contrast, from_ = -100, to = 100)
# Cscale.grid(row = 6, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

# ContrastB = tkinter.Button(top, text='Set Contrast', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
# ContrastB.grid(row = 6, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

# #Exposure
# Escale = Scale(top, variable = Exposure, from_ = -100, to = 100)
# Escale.grid(row = 7, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

# ExposureB = tkinter.Button(top, text='Set Exposure', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
# ExposureB.grid(row = 7, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

# #Sharpness
# SHscale = Scale(top, variable = Sharpness, from_ = -100, to = 100)
# SHscale.grid(row = 8, column = 0, sticky = W, pady = 0, padx = 7, ipadx=5)

# SharpnessB = tkinter.Button(top, text='Set Sharpness', width=12, background="#545451", foreground="white", borderwidth=2, font="calibri")
# SharpnessB.grid(row = 8, column = 1, sticky = W, pady = 0, padx = 7, ipadx=5)

# #Edge-Detection
# EDB = tkinter.Button(top, text='Apply Edge-detection', width=16, background="#545451", foreground="white", borderwidth=2, font="calibri")
# EDB.grid(row = 9, column = 0, columnspan=3, sticky = W, pady = 0, padx = 7, ipadx=5)

top.mainloop();
