models = []

def setup():
    global models
    size(1000, 1000, P3D)
    colorMode(HSB)
    
    for i in range(20):
        Obj_model = Model("RobotOBJ.obj",random(-250, 250), random(-250, 250), 0, random(20, 50), random(256)) 
        models.append(Obj_model)

    
    
def draw():
    global cube, cube2, cube3, Obj_model #Always call variables
    #colorMode(RGB)
    #blendMode(SUBTRACT)
    #fill(255, 1)
    #rect(0, 0, width*4, height*4)
    #blendMode(BLEND)
    colorMode(HSB)
    background(0)
    lights()
    strokeWeight(4)
    translate(width/2, height/2, ) #centre of screen
    
    # Callint the render method on the cube
    
    for Obj_model in models:
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
        self.sh.disableStyle()
        self.theta = 0
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.theta)
        rotateZ(PI)
        #rotateX(-HALF_PI)
        scale(self.s)
        stroke((self.h + mouseX) % 256, 255, 255)
        #noFill()
        shape(self.sh)
        popMatrix()
        self.theta += 0.01
