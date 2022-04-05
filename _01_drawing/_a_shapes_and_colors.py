import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    tooty = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    tooty.shape('turtle')
    # Set your turtle's speed using .speed(2)
    tooty.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    tooty.color('green')
    tooty.pencolor('blue')
    # Move your turtle forward using .forward(100)

    #tooty.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
    #tooty.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    for i in range(4):
        tooty.forward(100)
        tooty.left(90)
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    tooty.goto(50,200)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    tooty.begin_fill()
    tooty.circle(50, steps=3)
    tooty.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    for i in range(8):
        tooty.forward(30)
        tooty.right(360/8)




    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
