from turtle import *
ht()
speed(100)
bgcolor('black')
screensize(800,700)

for i in range(120):
	color('red')
	circle(i)
	color('orange')
	circle(i * 0.8)
	rt(3)
	fd(3)
	if i == 119:
		for j in range(119,0,-1):
			color('red')
			circle(j)
			color('orange')
			circle(j / 1.25)
			rt(3)
			fd(3)
			
setheading(270)
penup()
pensize(7)
fd(238)
ht()
pendown()
fd(450)
exitonclick()