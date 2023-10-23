def setup():
    size(200, 200)
    
def draw():
    background(0)
    
    ellipse(100, 100, 100, 100)
    ellipse(mouseX, mouseY, 20, 20)

def customDist(x1, y1, x2, y2):
    dx = x2- x1 #distance x
    dy = y2- y1 #distance y
    
    squared = dx*dx + dy*dy
    rooted  = sqrt(squared)
    return rooted


def mousePressed():
    if customDist(mouseX, mouseY, 100, 100) < 60:
        print("circle pressed")
            
