class defaultPaint:

    def __init__(self) -> None:
        self.points = []
        return None

    def render(self,canvas):
        print(self.points)
        arc = canvas.create_arc(20, 50, 190, 10, start=0, extent=110, fill="red")
        self.points = []
         

    def paintBase(self,event,canvas,prevPoint,currentPoint,stroke_color,stroke_size):
        x = event.x
        y = event.y
        currentPoint = [x,y]
        # canvas.create_oval(x , y , x +5 , y + 5 , fill="black")
        if prevPoint != [0,0] : 
            # canvas.create_polygon(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1],fill=stroke_color.get() , outline=stroke_color.get() , width=stroke_size.get())        
            canvas.create_oval(event.x,event.y,event.x +10,event.y+10,outline = "black",fill = "white",width = 2)
        prevPoint = currentPoint

        self.points.append([event.x,event.y])

        if event.type == "5" :
            prevPoint = [0,0]
        
        return prevPoint