def setup():
    global cube, cube2, cube3, Obj_model
    size(500, 500, P3D)
    colorMode(HSB)
    cube = Cube(0, 0, 0, 1, 60) # Creating the cube
    cube2 = Cube(0, 0, 0, 0.5, 100)
    cube3 = Cube (-200, -150, 0, 2, 200)
    Obj_model = Model("RobotOBJ.obj", 100, 0, 0, 75, 150)
    
    
def draw():
    global cube, cube2, cube3, Obj_model #Always call variables
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, 1)
    rect(0, 0, width*4, height*4)
    blendMode(BLEND)
    colorMode(HSB)
    lights()
    strokeWeight(4)
    translate(width/2, height/2, ) #centre of screen
    cube.render() # Callint the render method on the cube
    cube2.render()
    cube3.render()
    Obj_model.render()
    
    
    
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
        stroke((self.h + mouseX) % 256, 255, 255)
        noFill()
        box(100)
        popMatrix()
        self.theta += 0.01
        
class Model:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        scale(self.s)
        stroke((self.h + mouseX), 255, 255)
        noFill()
        shape(self.sh)
        popMatrix()
