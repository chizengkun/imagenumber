import turtle
r = 50
offset = 10
offrangle = 30
turtle.pensize(2)
for i in range(10):
    turtle.circle(r+ i*offset, 100+i*offrangle)

turtle.done()

''' 同心圆
r = 60
offset = 20

turtle.pensize(3)
for i in range(4):
    turtle.circle(r)
    r = r+offset

turtle.done()

'''