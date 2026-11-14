from turtle import *

ty = Turtle()
ty.speed(0)

def sym(x,y,symbol):
    ty.penup()
    ty.goto(x,y)
    ty.pendown()
    ty.color('gray')
    ty.write(symbol,font = ('Arial',18))

def square(x,y,color_2):
    ty.penup()
    ty.goto(x,y)
    ty.pendown()
    ty.color('gray',color_2)
    ty.begin_fill()
    for i in range (4):
        ty.forward(30)
        ty.right(90)
    ty.end_fill()

def kryg(x,y,r):
    ty.penup()
    ty.goto(x,y)
    ty.pendown()
    ty.color('gray')
    ty.begin_fill()
    ty.circle(r)
    ty.end_fill()

x = -200
square(x,-180,'green')
square(x+40*1,-180,'red')
square(x+40*2,-180,'blue')
square(x+40*3,-180,'black')
square(x+40*4,-180,'white')
square(x+40*5,-180,'orange')
square(x+40*6,-180,'skyblue')

square(x+40*8,-180,'black')
square(x+40*9,-180,'white')

sym(x+10,-240,'1')
sym(x+40*1+10,-240,'2')
sym(x+40*2+10,-240,'3')
sym(x+40*3+10,-240,'4')
sym(x+40*4+10,-240,'5')
sym(x+40*5+10,-240,'6')
sym(x+40*6+10,-240,'7')

sym(x+40*8+10,-240,'0')
sym(x+40*9+10,-240,'9')

sym(x,-50,'a')
sym(x,10,'s')
sym(x,65,'d')

kryg(x-30,-50,3)
kryg(x-30,5,6)
kryg(x-30,60,14)

ty.ht()
