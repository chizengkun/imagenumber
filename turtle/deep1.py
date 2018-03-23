import turtle

for x in range(4):
    turtle.up()
    turtle.goto(0,-(200- x*50))
    turtle.down()
    turtle.circle(200- x*50)

turtle.done()