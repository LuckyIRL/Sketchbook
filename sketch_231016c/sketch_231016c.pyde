def setup():
    size(500, 500)
    colorMode(HSB)
    background(0)
    noStroke()
    
def draw():
    
    x = 0
    for i in range(0, 500, 20):
        x+=30
        if(x==360):
            x=0
        fill(x,255,200)
        
        rect(i, 0, 20, 500)    
    
    
