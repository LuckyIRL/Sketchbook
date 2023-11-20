models = []

def setup():
    global models
    size(1000, 1000, P3D)
    colorMode(HSB)
    
    for i in range(100):
        car52_model = Model("car52.obj",random(-500, 500), random(-500, 500), random(-250, 250), random(50, 250), random(256)) 
        models.append(car52_model)

    
    
def draw():
    global models #Always call variables
    
    pushMatrix()
    textAlign(RIGHT)
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, 1)
    rect(0, 0, width*4, height*4)
    blendMode(BLEND)
    colorMode(HSB)
    background(0)
    lights()
    strokeWeight(4)
    translate(width/2, height/2, 100 ) #centre of screen
    
    # Callint the render method on the cube
    
    for car52_model in models:
        car52_model.render()
    popMatrix()
    
# A class consists of fields and methods    

        
class Model:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.theta = random(TWO_PI)
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        #rotateY(self.theta)
        #rotateZ(HALF_PI)
        rotateX(-HALF_PI)
        scale(1.0 + noise(self.theta * 2) * 50)
        stroke((self.h + mouseX) % 256, 255, 255)
        noFill()
        shape(self.sh)
        popMatrix()
        self.theta += 0.01
        self.pos.z += 1 
        
        if self.pos.z > 600:
            self.pos.z = 0
    
