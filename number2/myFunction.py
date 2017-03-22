def polygon(t,sides,distance): #the function output(polygon) and the input(t,sides,distance)
    for times in range(sides): #a loop
        t.forward(distance) # moving turtle forward
        t.left(360/sides) # moving turtle left 

def star(t): # function output(star) and function input(t) or turtle
    for times in range(255): #a loop
        t.begin_fill()
        t.penup
        m=(255-times,255-times,0) #colormode or the color changing as the loop contiune
        h=(0,255-times,255-times)
        t.color(m)# the color which turtle is set as
        t.width(5)# the thickness of the lines created by turtle
        polygon(t,3,255-times) #function 
        t.left(20)# move turtle left by 20 degrees
        t.end_fill()
        t.pendown
        t.color(h)
        t.width(2.5)
        t.circle(times)# draw the circle
        t.left(20)

#the whole function is about drawing triangle,and rotating left, as it is also drawing a circle and rotating it left
