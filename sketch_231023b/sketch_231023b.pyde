def setup():
    size(500,500)
    
    a = 1
    b = 1
    for i in range (1000):
        ab = a + b
        print(i)
        a = b #
        b = ab
        
def draw():
    pass
