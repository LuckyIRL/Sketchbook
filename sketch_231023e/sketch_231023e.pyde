import turtle

# Set up the turtle screen
window = turtle.Screen()
window.bgcolor("white")

# Create a turtle for drawing
flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)  # Set drawing speed

# Draw the yellow center
flower.color("yellow")
flower.begin_fill()
flower.circle(100)
flower.end_fill()

# Draw the blue petals using loops
flower.color("blue")
for _ in range(10):
    flower.begin_fill()
    for _ in range(2):
        flower.circle(50, 60)
        flower.left(120)
    flower.end_fill()
    flower.right(36)  # Rotate to the next petal position

# Close the turtle graphics window on click
window.exitonclick()
