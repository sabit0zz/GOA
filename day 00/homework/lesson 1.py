from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing door

forward(70)
color("yellow")
left(90)
forward (120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(30)
penup()
color("blue")
forward (40)
begin_fill()
left(90)
forward(25)
pendown()
forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
end_fill()
right(90)
penup()
forward(110)
pendown()
begin_fill()
forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
end_fill()

exitonclick()