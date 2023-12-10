from tkinter import colorchooser


class selector:

    def selectColor(i,stroke_color,previousColor,previousColor2):
        selectedColor = colorchooser.askcolor("blue" , title="Select Color")
        if selectedColor[1] == None :
            stroke_color.set("black")
        else:
            stroke_color.set(selectedColor[1])
            previousColor2.set(previousColor.get())
            previousColor.set(selectedColor[1])