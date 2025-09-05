def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_around()
    
    
def turn_loop():
    turn_left()
    move()
    turn_right()
    if wall_in_front():
        turn_loop()
    else:   
     move()
     turn_right()
     while not wall_in_front():
        move()
     turn_left()

while not at_goal():
    
    if wall_in_front():
        turn_loop()
    
    else:
        move()
    
    
        
        
        


    
    