import turtle

win = turtle.Screen()
win.bgcolor("White")
win.title("Belajar Turtle")
win.setup(width=750, height=500)

t = turtle.Turtle()
t.shape("turtle")
t.color("red")

t.speed(1)

# menulis huruf L
t.penup()
t.backward(100)
t.pendown()
t.backward(100)
t.goto(-200,200)
t.penup()

# menulis huruf W
t.forward(200)
t.pendown()
t.goto(0,0)
t.left(70)
t.forward(200)
t.right(140)
t.forward(200)
t.left(160)
t.forward(200)

turtle.done()
