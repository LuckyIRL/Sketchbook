def setup():
    global cube, cube2, cube3
    size(500, 500, P3D)
    colorMode(HSB)
    cube = Cube(0, 0, 0, 1, 60) # Creating the cube
    cube2 = Cube(0, 0, 0, 0.5, 100)
    cube3 = Cube (-200, -150, 0, 2, 200)
    
def draw():
    global cube, cube2, cube3 #Always call variables
    background(0)
    lights()
    translate(width/2, height/2, ) #centre of screen
    cube.render() # Callint the render method on the cube
    cube2.render()
    cube3.render()
# A class consists of fields and methods    
class Cube:
    
    # Constructor
    def __init__(self, x, y, z, s, h):
        #These are now fields!! that's what the 'self' word does.
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.theta = 0
        
        
    def render(self):
        pushMatrix()
        rotateY(self.theta)
        rotateX(self.theta)
        translate(self.pos.x, self.pos.y, self.pos.z)
        scale(self.s)
        stroke(self.h, 255, 255)
        noFill()
        box(100)
        popMatrix()
        self.theta += 0.01
