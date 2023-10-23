def setup():
    fullScreen()
    #size(1000,1000)
    global cx 
    global cy
    global px
    global py
    global r
    global theta
    global x
    global y
    global c
    cx = width / 2
    cy = height / 2
    background(0)
    colorMode (HSB)
    px = cx
    py = cy
    
cx = 0 
cy = 0 
r = 1
theta = 0
c = 0

px = 0
py = 0

def draw():
    global cx 
    global cy
    global px
    global py
    global r
    global theta
    global x
    global y
    global c
    x = cx + sin(theta) * r
    y = cy + cos(theta) * r
    
   
    
    stroke(c, 255, 255)
    strokeWeight(mouseX)
    line(px, py, x, y)
    r = r + 1
    c = (c + 1) % 142
    theta = theta + 2.65
    
    px = x
    py = y
    x = x + 1
