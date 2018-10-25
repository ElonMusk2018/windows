import tkinter as tk
import turtle

def half(t,size,x,y,color):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color(color)
	for i in range (1,31):
		t.forward(size)
		t.right(6)


def circle(t,size,x,y,color):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color(color)
	for i in range (1,61):
		t.forward(size)
		t.right(6)
	
def logan():
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	circle(t,5,100,100,"#ff0000")
	circle(t,5,-100,100,"#0000ff")
	circle(t,3,0,0,"#0000ff")
	half(t,10
	,0,-100,"#0000ff")
	
logan()
holdit = input("press to exit")
	
	
	
	
