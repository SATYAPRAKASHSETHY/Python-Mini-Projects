from turtle import *
screensize(800,600)
speed(100)
ht()
color('cyan')
bgcolor('black')
b = 200
penup()
fd(280)
pendown()
while b > 0:
	lt(b)
	fd(b * 3)
	b = b - 1
mainloop()