def setup():
    global rectSize
    rectSize = 100
    rectMode(CENTER)
    
    size(500, 500)
    background(0)

def draw():
    global rectSize
    background(0)
    
    
    if mousePressed:
            rectSize = rectSize + 1
        
    else:
            rectSize = rectSize - 1
    rectSize = constrain (rectSize, 0, 250)
    fill(mouseX, 142, mouseY)    
    rect(height /2, width /2, rectSize, rectSize,)
