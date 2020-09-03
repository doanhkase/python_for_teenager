import turtle

t = turtle.Pen()
t.speed(7)

#body
t.left(30)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(25)
t.right(130)

#leg left
t.forward(80)
t.left(45)
t.forward(70)
t.right(90)
t.forward(40)
t.left(90)
t.forward(30)
t.left(90)
t.forward(10)
t.right(90)
t.forward(10)
t.left(180)
t.forward(10)
t.right(90)
t.forward(10)
t.right(90)
t.forward(10)
t.left(180)
t.forward(10)
t.right(90)
t.forward(10)
t.right(90)
t.forward(10)
t.left(180)
t.forward(10)
t.right(90)
t.forward(10)
t.left(90)
t.forward(30)
t.forward(70)
t.right(45)
t.forward(80)

#leg right
t.right(50)
t.forward(50)
t.right(135)
t.forward(80)
t.left(105)
t.forward(70)
t.left(45)
t.forward(15)
t.right(90)
t.forward(10)
t.left(90)
t.forward(10)
t.left(180)
t.forward(10)
t.left(90)
t.forward(10)
t.left(90)
t.forward(10)
t.right(180)
t.forward(10)
t.left(90)
t.forward(10)
t.left(90)
t.forward(10)
t.left(180)
t.forward(10)
t.left(90)
t.forward(10)
t.right(90)
t.forward(30)
t.right(90)
t.forward(40)
t.right(90)
t.forward(15)

#ball
t.up()
t.forward(100)
t.right(90)
t.forward(40)
t.left(180)
t.down()
t.circle(30)
t.up()
t.forward(40)
t.left(90)
t.forward(100)

#arm right
t.right(45)
t.forward(70)
t.right(105)
t.forward(80)
t.right(45)
t.forward(25)
t.left(90)
t.forward(150)
t.right(115)
t.down()
t.forward(75)
t.right(90)
t.forward(100)
t.right(90)
t.circle(10)
t.right(90)
t.forward(100)
t.left(90)
t.forward(75)

#head
t.left(25)
t.forward(50)
t.right(90)
t.up()
t.forward(15)
t.right(90)
t.down()
t.circle(35)
t.up()
t.left(90)
t.forward(40)
t.right(90)
t.down()
t.circle(5)
t.up()
t.forward(20)
t.down()
t.circle(5)

#arm left
t.up()
t.left(180)
t.forward(20)
t.left(90)
t.forward(55)
t.right(90)
t.forward(50)
t.left(30)
t.down()
t.forward(75)
t.left(25)
t.forward(80)
t.right(90)
t.circle(10)

turtle.done()