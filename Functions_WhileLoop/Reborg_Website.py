# Go to Reeborg Website and paste this code
# Hurdle 1 in alone...

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_around()


def turn_loop():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range (4):
    turn_loop()

print("You are at correct x and y position")

    
    