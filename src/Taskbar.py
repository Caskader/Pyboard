from tkinter import *


def initTaskbar(frame1,usePencil,useEraser,stroke_size,options,selectColor,stroke_color,previousColor,previousColor2,saveImage,createNew,clear,settings,about,textValue):
    toolsFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN , borderwidth=3)
    toolsFrame.grid(row=0 , column=0 )

    pencilButton = Button(toolsFrame , text="Pencil" , width=10 , command=usePencil)
    pencilButton.grid(row=0 , column=0)
    eraserButton = Button(toolsFrame , text="Eraser" , width=10 , command=useEraser)
    eraserButton.grid(row=1 , column=0)
    toolsLabel = Label(toolsFrame , text="Tools", width=10)
    toolsLabel.grid(row=3 , column=0)

    # sizeFrame 

    sizeFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN , borderwidth=3 )
    sizeFrame.grid(row=0 , column=1 )

    defaultButton = Button(sizeFrame , text="Default" , width=10 , command=usePencil)
    defaultButton.grid(row=0 , column=0)
    sizeList = OptionMenu(sizeFrame , stroke_size , *options)
    sizeList.grid(row=1 , column=0)
    sizeLabel = Label(sizeFrame , text="Size", width=10)
    sizeLabel.grid(row=2 , column=0)

    # colorBoxFrame

    colorBoxFrame = Frame(frame1 , height=100 , width=100 ,relief=SUNKEN , borderwidth=3 )
    colorBoxFrame.grid(row = 0 , column=2)

    colorBoxButton = Button(colorBoxFrame , text="Select Color" , width=10 , command=selectColor)
    colorBoxButton.grid(row=0 , column=0)
    previousColorButton = Button(colorBoxFrame , text="Previous" , width=10 , command=lambda:stroke_color.set(previousColor.get()))
    previousColorButton.grid(row=1 , column=0)
    previousColor2Button = Button(colorBoxFrame , text="Previous2" , width=10 , command=lambda:stroke_color.set(previousColor2.get()))
    previousColor2Button.grid(row=2 , column=0)

    # colorsFrame

    colorsFrame = Frame(frame1, height=100 , width=100, relief=SUNKEN , borderwidth=3)
    colorsFrame.grid(row = 0 , column=3)

    redButton = Button(colorsFrame , text="Red" , bg="red" , width=10 , command=lambda: stroke_color.set("red"))
    redButton.grid(row=0 , column=0)
    greenButton = Button(colorsFrame , text="Green" , bg="green" , width=10 , command=lambda: stroke_color.set("green"))
    greenButton.grid(row=1 , column=0)
    blueButton = Button(colorsFrame , text="Blue" , bg="blue" , width=10 , command=lambda: stroke_color.set("blue"))
    blueButton.grid(row=2 , column=0)
    yellowButton = Button(colorsFrame , text="Yellow" , bg="yellow" , width=10 , command=lambda: stroke_color.set("yellow"))
    yellowButton.grid(row=0 , column=1)
    orangeButton = Button(colorsFrame , text="Orange" , bg="orange" , width=10 , command=lambda: stroke_color.set("orange"))
    orangeButton.grid(row=1 , column=1)
    purpleButton = Button(colorsFrame , text="Purple" , bg="purple" , width=10 , command=lambda: stroke_color.set("purple"))
    purpleButton.grid(row=2 , column=1)

    # saveImageFrame

    saveImageFrame = Frame(frame1, height=100 , width=100, relief=SUNKEN , borderwidth=3)
    saveImageFrame.grid(row = 0 , column=4)

    saveImageButton = Button(saveImageFrame , text="Save" , bg="white" , width=10 , command=saveImage)
    saveImageButton.grid(row=0 , column=0)
    newImageButton = Button(saveImageFrame , text="New" , bg="white" , width=10 , command=createNew)
    newImageButton.grid(row=1 , column=0)
    clearImageButton = Button(saveImageFrame , text="Clear" , bg="white" , width=10 , command=clear)
    clearImageButton.grid(row=2 , column=0)

    # helpSettingFrame

    helpSettingFrame = Frame(frame1, height=100 , width=100, relief=SUNKEN , borderwidth=3)
    helpSettingFrame.grid(row = 0 , column=5)

    helpButton = Button(helpSettingFrame , text="Help" , bg="white" , width=10 , command=help)
    helpButton.grid(row=0 , column=0)
    settingButton = Button(helpSettingFrame , text="Settings" , bg="white" , width=10 , command=settings)
    settingButton.grid(row=1 , column=0)
    aboutButton = Button(helpSettingFrame , text="About" , bg="white" , width=10 , command=about)
    aboutButton.grid(row=2 , column=0)

    # textFrame

    textFrame = Frame(frame1, height=100 , width=200, relief=SUNKEN , borderwidth=3)
    textFrame.grid(row = 0 , column=6)

    textTitleButton = Label(textFrame , text="Write you Text here:" , bg="white" , width=20 )
    textTitleButton.grid(row=0 , column=0)
    entryButton = Entry(textFrame, textvariable=textValue, bg="white" , width=20 )
    entryButton.grid(row=1 , column=0)
    clearButton = Button(textFrame , text="Clear" , bg="white" , width=20 , command=lambda:textValue.set(""))
    clearButton.grid(row=2 , column=0)

    # noteFrame

    noteFrame = Frame(frame1, height=100 , width=200, relief=SUNKEN , borderwidth=3)
    noteFrame.grid(row = 0 , column=7)

    textTitleButton = Text(noteFrame, bg="white" , width=40 , height=4 )
    textTitleButton.grid(row=0 , column=0)
    print(stroke_size)
