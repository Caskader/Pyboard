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


# def startPaint(event):

    

#     global prevPoint
#     global currentPoint
    
# def l(i):
#     print("hi")
       

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

# initializing taskbar

initTaskbar(frame1,usePencil,useEraser,stroke_size,options,selectColor,stroke_color,previousColor,previousColor2,saveImage,createNew,clear,settings,about,textValue)

# Frame - 2 - Canvas

frame2 = Frame(root , height=500 , width=1100 , bg="yellow")
frame2.grid(row=1 , column=0)

main_canvas = Canvas(frame2 , height=500 , width=1100 , bg="white" )
main_canvas.grid(row=0 , column=0)


# binding the event for writting text
# main_canvas.bind("<Button-2>", writeText)
root.resizable(True , True)

# added new Graphics handler object to handle
class GraphicsHandler:

    def __init__(self,main_canvas,drawing_canvas) -> None:
        super()
        global prevPoint
        global currentPoint
    

        self.drawing_canvas = drawing_canvas
        self.penDown = 0
        self.drawing_canvas.bind("<B1-Motion>",self.setPenDown)
        self.drawing_canvas.bind("<ButtonRelease-1>", self.setPenUp)
        self.prevPoint = prevPoint

        while True:
            # arc = canvas.create_arc(20, 50, 190, 10, start=0, extent=110, fill="red")    
            if int(self.penDown) == 1:
                self.prevPoint = defaultBrush.paintBase(self.event,self.drawing_canvas,self.prevPoint,currentPoint,stroke_color,stroke_size)

            self.penDown = 0
            main_canvas.pack()
            root.update()
            time.sleep(0.01)

    def setPenDown(self,event):
        self.penDown = 1
        self.event = event
    
    def setPenUp(self,event):
        self.penDown = 0
        self.prevPoint = [0,0]
        defaultBrush.render(self.drawing_canvas)

g = GraphicsHandler(main_canvas,main_canvas)
# prevPoint = g.prevPoint

root.mainloop()