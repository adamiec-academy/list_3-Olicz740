from turtle import *
speed("fast")
penup()
goto(-100,0)
pendown()

def square(side):
    left(90)
    for i in range(4):
        forward(side)
        right(90)

def square_pyramid(side, gap):

    height = 0
    for _ in range(5):
        height += side
        square(side)
        forward(side)
        right(90)
        forward(gap/2)
        side = side - gap

    penup()
    forward(side + (gap/2) * 5)
    right(90)
    forward(height)
    left(90)
    pendown()

def star(side, gap):
    for i in range(6):
        square_pyramid(side, gap)
        right(360/6)

print(star(50,10))

exitonclick()
