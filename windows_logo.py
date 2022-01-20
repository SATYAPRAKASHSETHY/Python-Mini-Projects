from turtle import *
screensize(800,600)
ht()	#hide turtle
speed(10)

bgcolor('white')
penup()
goto(-50,60)
pendown()
color('#00adef')
begin_fill()
goto(100,100)
goto(100,-100)
goto(-50,-60)
goto(-50,60)
end_fill()

penup()
goto(15,100)
pendown()
color('white')	#keep same color as bgcolor
width(10)
goto(15,-100)

penup()
goto(100,0)
pendown()
goto(-100,0)

mainloop()