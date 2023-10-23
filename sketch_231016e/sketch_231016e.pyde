def setup():
    size(500, 500)
    colorMode(HSB)
    background(0)
    noStroke()
    
def draw():    
    num_circles = 7
    gap = width/ float(num_circles)
    rad = gap / 2
    cgap = 10
    start_c = mouseX /2
    spacing = rad
    num_rows = 
    for i in range (
    for i in range (num_circles):
        x = rad + (gap * i)
        c = (start_c +(i * cgap)) % 256
        
        fill(c, 255, 255)
        circle(x, spacing, gap)
