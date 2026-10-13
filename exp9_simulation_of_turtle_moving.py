import turtle

# Initialize turtle agent
t = turtle.Turtle()
t.speed(2)

# Execute robotic trajectory
t.forward(100)      # Advance 100 units
t.left(90)          # Turn left 90 degrees
t.forward(100)      # Advance 100 units
t.right(45)         # Turn right 45 degrees
t.backward(100)     # Reverse 100 units

# Conclude simulation
t.hideturtle()
turtle.done()
