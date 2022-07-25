import turtle

turtle.shape('turtle')
my_turtle = turtle.Turtle()

wn = turtle.Screen()
def square(a, b):
    for i in range(4):
        my_turtle.forward(a)
        my_turtle.right(b)
    

for i in range(36):
    square(100, 90)
    turtle.pencolor('red')
    my_turtle.right(10)

    

wn.exitonclick()