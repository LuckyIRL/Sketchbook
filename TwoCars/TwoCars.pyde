models = []

def setup():
    global models
    #fullScreen(P3D)
    size(1000, 1000, P3D)
    colorMode(HSB)
    
    for i in range(4):
        car52_model = Model("CarModel52.obj",0,0,0, 10, random(256))
        models.append(car52_model)
        
        for i in range(4):
            model52 = Model("Model52.obj",200,100,0, 50, random(256))
            models.append(model52)
    
    
    
def draw():
    global models #Always call variables
    
    pushMatrix()
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, 7)
    rect(0,0, width*2, height*4)
    blendMode(BLEND)
    colorMode(HSB)
    #background(0)
    lights()
    strokeWeight(4)
    translate(width/2.05, height/1.9) #centre of screen
    
    # Callint the render method on the cube
    
    for car52_model in models:
        car52_model.render()
    for model52 in models:
        model52.render()
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
        #textAlign(CENTER)
        translate(self.pos.x, self.pos.y, self.pos.z)
        #rotateY(self.theta)
        rotateZ(PI)
        #rotateX(-HALF_PI)
        #scale(1.0 + noise(self.theta * 2) * 50)
        scale(self.s)
        stroke((self.h + mouseX) % 256, 255, 255)
        noFill()
        shape(self.sh)
        popMatrix()
        #self.theta += 0.01
        self.pos.z += 10
        
        if self.pos.z > 5000:
            self.pos.z = 0
 
    
class CarModels:
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
