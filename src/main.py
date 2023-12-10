from tkinter import *
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog
from tkinter import messagebox
import time

# importing the files
import color_selector
import paintBrush;
from Taskbar import initTaskbar

#initializing 
root = Tk()
root.title("Paint App")
root.geometry("1100x600")

color = color_selector.selector()
defaultBrush = paintBrush.defaultPaint()

# -------------- variables --------------------

# stroke size options 
options = [1,2,3,4,5,10]

stroke_size = IntVar()
stroke_size.set(1)

stroke_color = StringVar()
stroke_color.set("black")

previousColor = StringVar()
previousColor.set("white")

previousColor2 = StringVar()
previousColor2.set("white")

# variables for pencil 
prevPoint = [0,0]
currentPoint = [0,0] 

# variable for text
textValue = StringVar()

brushDown = 0



# --------------------- functions -------------------------

def usePencil():
    stroke_color.set("black")
    canvas["cursor"] = "arrow"

def useEraser():
    stroke_color.set("white")
    canvas["cursor"] = DOTBOX

def selectColor():
    color.selectColor(stroke_color,previousColor,previousColor2)


def startPaint(event):

    

    global prevPoint
    global currentPoint
    
def l(i):
    print("hi")
       

def saveImage():
    try:
        fileLocation = filedialog.asksaveasfilename(defaultextension="jpg")
        x = root.winfo_rootx()
        y = root.winfo_rooty()+100
        img = ImageGrab.grab(bbox=(x,y,x+1100,y+500))
        img.save(fileLocation)
        showImage = messagebox.askyesno("Paint App" , "Do you want to open image?")
        if showImage:
            img.show()

    except Exception as e:
        messagebox.showinfo("Paint app: " , "Error occured")


def clear():
    if messagebox.askokcancel("Paint app" , "Do you want to clear everything?"):
        canvas.delete('all')

def createNew():
    if messagebox.askyesno("Paint app" , "Do you want to save before you clear everything?"):
        saveImage()
    clear()

def help():
    helpText = "1. Draw by holding right button of mouse to create dotted lines.\n2.Click scroll well to put text on Canvas.\n3. Click on Select Color Option select specific color\n4. Click on Clear to clear entire Canvas"
    messagebox.showinfo("Help" , helpText)

def settings():
    messagebox.showwarning("Settings" , "Not Available")

def about():
    messagebox.showinfo("About" , "This paint app is best!")

def writeText(event):
    canvas.create_text(event.x , event.y , text=textValue.get())
# ------------------- User Interface -------------------

# Frame - 1 : Tools 

frame1 = Frame(root , height=100 , width=1100 )
frame1.grid(row=0 , column=0, sticky=NW)

# toolsFrame 

initTaskbar(frame1,usePencil,useEraser,stroke_size,options,selectColor,stroke_color,previousColor,previousColor2,saveImage,createNew,clear,settings,about,textValue)

# Frame - 2 - Canvas

frame2 = Frame(root , height=500 , width=1100 , bg="yellow")
frame2.grid(row=1 , column=0)

canvas = Canvas(frame2 , height=500 , width=1100 , bg="white" )
canvas.grid(row=0 , column=0)

# canvas.create_rectangle(0,0,2,2,"black","black",10)
canvas.bind("<ButtonRelease-1>", startPaint)
canvas.bind("<B3-Motion>" , l)
canvas.bind("<Button-2>", writeText)
root.resizable(True , True)
s = 0


class GraphicsHandler:

    def __init__(self,canvas) -> None:
        super()
        global prevPoint
        global currentPoint
    
        self.penDown = 0
        canvas.bind("<B1-Motion>",self.ok)
        self.prevPoint = prevPoint
        a= 0 
        while True:
            # arc = canvas.create_arc(20, 50, 190, 10, start=0, extent=110, fill="red")    
            defaultBrush.render(canvas)
            if int(self.penDown) == 1:
                if a>1:
                    self.prevPoint = defaultBrush.paint(self.event,canvas,self.prevPoint,currentPoint,stroke_color,stroke_size)
                else:
                    self.prevPoint = [0,0]
                    a+=1
                    arc = canvas.create_arc(20, 50, 190, 10, start=0, extent=110, fill="red")    
                
                    self.prevPoint = defaultBrush.paint(self.event,canvas,self.prevPoint,currentPoint,stroke_color,stroke_size)
                

            if self.penDown == 0:
                a = 0

            self.penDown = 0
            canvas.pack()
            root.update()
            time.sleep(0.01)

    def ok(self,event):
        self.penDown = 1
        self.event = event

g = GraphicsHandler(canvas)
prevPoint = g.prevPoint