from turtle import *
ht()
speed(50)
bgcolor('black')

screensize(800,600)

penup()
goto(0,-280)

pendown()
color('#bc2a8d')
#pencolor('#bc2a8d')
begin_fill()
circle(300)
end_fill()
pencolor('white')
width(23)
speed(3)
penup()
goto(160,-100)
pendown()
lt(90)

for i in range(4):
	fd(250)
	circle(34,90)	
penup()
goto(85,30)
pendown()
circle(80,360)

penup()
goto(110,130)
pendown()
circle(7,360)

done()