import turtle
from turtle import *
import time
#turtle.speed("fastest")
turtle.pensize(2)
#bgcolor("black")
colors = ["red","yellow","purple","blue"]
tracer(False)
for x in range(400):
    turtle.forward(2*x)
    #turtle.color(colors[x%4])
    turtle.left(91)    #  角度 的控制  参数不同 ，图像不同
tracer(True)
done()