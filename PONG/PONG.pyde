#global
left_y = 300
right_y = 300
ball_x = 400
ball_y = 300
# speed of ball
dx = -1
dy = 1

score_l = 0
score_r = 0

def setup():
    size(800, 600)
    frameRate(60)
    
def draw ():
    #UPDATES
    global ball_x, ball_y, dx, dy, score_l, score_r
    
    #Check for bounce at bottom of screen
    if ball_y > height -10 or ball_y < 10:
        
        dy = dy *- 1

    #Touch left side - Right player score
    if ball_x < 0:
        score_r += 1
        # TODO move ball to centre
        
    #Bounce Paddle
    if ball_x < 70:
        if ball_y > left_y and ball_y < (left_y + 50):
         dx = 1    
                                
    
    #Move ball
    ball_x = ball_x + dx
    ball_y = ball_y + dy
    
    background(0)
       
    rect (30, left_y, 20,70) # P1 LeftPaddle
    rect (750, right_y, 20,70) # P2 RightPaddle
    
    ellipse (ball_x, ball_y, 20,20) # Ball
    
    textSize(40)
    textAlign(CENTER)
    text("SCORE", 400, 50) # Scores
    text("0" , 30, 50) #P1
    text(score_r , 750, 50) #P2 
  
def keyPressed():
    global left_y, right_y
    
    if key == "s":
        # s key is down
        left_y = left_y + 5 
        
    elif key == "w":
        # w key is up
        left_y = left_y - 5 
            
    elif key == "o":
        # o key is down
        right_y = right_y - 5 
        
    elif key == "l":
        # l key is down
        right_y = right_y + 5
