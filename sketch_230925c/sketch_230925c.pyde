def setup ():
    global x
    global y
    global a
    global b
    global c
    global d
    global e
    global f
    
    background(0)
    x = width / 2
    y = height/ 2
    b = width / 2
    w = height/ 2
    size (500, 500)

x = 0
y = 0
    
            
def draw():
    background(0)
    global x
    global y
    fill (0, 255, 0)
    circle (x, y, 200)
    x = x +1 
    y = y -1


    global b
    global w   
    fill (0, 0, 255)
    circle (x, y, 200)
    b = b -1
    w = w -1
    




    
