#############################################
Take a look at Turtle class
from the official python documentation
#################################




import turtle

def draw_square(v):
    for i in range(1,5):
        v.forward(100)
        v.right(90)

def draw_tri(v):
    for i in range(1,4):
        v.forward(200)
        v.left(120)

def draw_flower(v):
    for i in range(1,73):
        v.right(5)
        for j in range(1,4):
            v.forward(50)
            v.right(120)
    v.forward(250 )

def flower_of_life(v):
    for i in range(1,5):
        v.setpos(60,30)
        v.right(90)
        v.circle(50)
    v.shape("turtle")
    #v.forward(250)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("yellow")

#    brad = turtle.Turtle()
 #   brad.shape("turtle")
  #  brad.color("blue")
   # brad.speed(10)
    #for i in  range(1,20):
     #   draw_square(brad)
      #  brad.right(20)

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("Yellow")
    #angie.circle(100)

    #megh = turtle.Turtle()
    #megh.shape("classic")
    #megh.color("green")

    #draw_tri(megh)

    sun = turtle.Turtle()
    sun.color('red')
    sun.speed(10)
    flower_of_life(sun)


    window.exitonclick()


draw_shapes()
