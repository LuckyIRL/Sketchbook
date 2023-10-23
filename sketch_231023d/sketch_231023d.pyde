def setup():
    size(500,500)
    colorMode(HSB)
    cx = width/2
    cy = height/2
    
cx = 0
cy = 0    
r  = 150    
def draw ():
    global cx, cy, r
    num = 12 
    theta = TWO_PI/12
    
    background (0)
    noStroke()
    for i in range (num):
        angle = theta * i
        c = (i / float(num)) * 255
        print(c)
        fill(c, 255, 255)
        x = cx + sin(angle) * r
        y = cy + cos(angle) * r
        circle (x, y, 20)
