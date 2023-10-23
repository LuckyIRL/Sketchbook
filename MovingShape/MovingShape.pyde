def setup():
    global x
    x = 0
    
    size(500,500)
    background(0)
    
def draw():
    global x
    
    background(0)
    fill(mouseX,50, mouseY)
    rect(x, 25, 50, 50)
    
    if x > 500:
        x = -50
        x = x - 1
    else:
        x = x + 1
