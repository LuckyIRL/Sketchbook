def setup(): #runs at the start
    fullScreen()
    global x
    global y
    global a
    global b
    global c
    global d
    global e
    global f
    colorMode(RGB)
    size(500,500)
    background(0)
    x = width / 2
    y = height / 2
    a = width / 2
    b = height / 2
    c = width / 2
    d = height / 2
    e = width / 2
    f = height / 2


x=0
y=0

def draw():
    #xy
    global x
    global y
    fill(mouseY, mouseX, 200)
    circle(x , y, 200)
    x = x+1
    y = y+1
   
    #ab
    global a
    global b
    fill(mouseX, mouseY, 200)
    circle(a , b, 150)
    a = a+1
    b = b-1
   
    #cd
    global c
    global d
    fill(210, mouseX, mouseY )
    circle(c , d, 100)
    c = c-1
    d = d+1
   
    #ef
    global e
    global f
    fill(mouseY, 102, mouseX)
    circle(e , f, 50)
    e = e-1
    f = f-1
