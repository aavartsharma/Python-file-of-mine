from turtle import *

a="I"
c="O"
b="L"
e="E"
f="Y"
g="U"
d="V"
message=a+" "+b+c+d+e+" "+f+c+g

hideturtle()
speed(5)
penup()
goto(0,-300)
pendown()
color('red')
bgcolor("pink")
begin_fill()
pensize(20)
left(50)
forward(530)
circle(200,200)
right(140)
circle(200,200)
forward(530)

end_fill()
penup()
goto(-425, -750)
pendown()
write(message, font=("Playpen Sans", 30, "bold"))
penup()
speed(1)
forward(500)
#delay(10000000)
text=textinput("hi","Do you love me?")

    
exitonclick()
