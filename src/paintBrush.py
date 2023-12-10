class defaultPaint:

    def __init__(self) -> None:
        
        pass

    def render(i,canvas):
        arc = canvas.create_arc(20, 50, 190, 10, start=0, extent=110, fill="red") 

    def paint(i,event,canvas,prevPoint,currentPoint,stroke_color,stroke_size):
        x = event.x
        y = event.y
        currentPoint = [x,y]
        # canvas.create_oval(x , y , x +5 , y + 5 , fill="black")
        if prevPoint != [0,0] : 
            canvas.create_polygon(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1],fill=stroke_color.get() , outline=stroke_color.get() , width=stroke_size.get())        
            # canvas.create_oval(110,10,210,110,outline = "black",fill = "white",width = 2)
        prevPoint = currentPoint

        if event.type == "5" :
            prevPoint = [0,0]
        
        return prevPoint