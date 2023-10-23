def setup():
    global y
    global xdir
    size (500, 500)
    background(0)
    y = height/2
    
w = 50
hw = w/2
x = hw
y = 0
xdir = 1
        
def draw():
    noStroke () 
    fill(x/ 2, 255, 255);
    circle(x, y, w);
    x = x +1
    
    if x == width + hw:
        xdir = x - 1
