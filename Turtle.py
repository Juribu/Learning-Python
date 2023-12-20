import turtle   

wn = turtle.Screen()    
wn.bgcolor("lightblue")     # set the window background color

alex = turtle.Turtule()     # give name for the object
alex.color("Red")           # give color for Alex
alex.pensize(3)             # set the width of her pen
alex.shape("turtle")

dist = 5                    # the distance alex travel each time        
alex.up()                   # lift alex up so it does not leave trail on paper
for _ in range(3):          # make alex do the set of command 3 times
    alex.stamp()            # leaves an impression on the canvas
    alex.forward(150)
    alex.left(90)
    alex.forward(75)
    dist += 2

wn.exitonclick()            # wait for a user click on the canvas