from turtle import *
from paint_module import *

t = Turtle()
t.pensize(5)
t.shape('circle')
t.speed(0)
t.color('red')






def green():
    t.color('green')

def red():
    t.color('red')

def blue():
    t.color('blue')

def black():
    t.color('black')

def white():
    t.color('white')

def sky_blue():
    t.color('skyblue')

def orange():
    t.color('orange')



def right():
    t.goto(t.xcor()+5,t.ycor())

def left():
    t.goto(t.xcor()-5,t.ycor())

def up():
    t.goto(t.xcor(),t.ycor()+5)

def down():
    t.goto(t.xcor(),t.ycor()-5)

def size_1():
    t.pensize(5)

def size_2():
    t.pensize(10)

def size_3():
    t.pensize(25)

def white_bg():
    scr.bgcolor('white')

def black_bg():
    scr.bgcolor('black')



def go(x,y):
    t.goto(x,y)


def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()


t.ondrag(go)

scr = t.getscreen()
scr.onscreenclick(move)
scr.setup(500,500)
scr.tracer(0)


scr.listen()
scr.onkey(green,'1')
scr.onkey(red,'2')
scr.onkey(blue,'3')
scr.onkey(black,'4')
scr.onkey(white,'5')
scr.onkey(orange,'6')
scr.onkey(sky_blue,'7')


scr.onkey(up,'Up')
scr.onkey(right,'Right')
scr.onkey(left,'Left')
scr.onkey(down,'Down')


scr.onkey(size_1,'a')
scr.onkey(size_2,'s')
scr.onkey(size_3,'d')

scr.onkey(white_bg,'9')
scr.onkey(black_bg,'0')



while True:
    scr.update()
