from turtle import *

# I've implemented this function for you; do not edit it.
def tree( trunkLength, angle, levels ):
    left(90)
    sidewaysTree(trunkLength, angle, levels)

# This is the function you have to implement.
def sidewaysTree(trunkLength, angle, levels):
    """ draws a sideways tree
        trunklength = the length of the first line drawn ("the trunk")
        angle = the angle to turn before drawing a branch
        levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
        forward(trunkLength) # draw line segment of trunkLength
        left(angle) # turn left by angle
        sidewaysTree(trunkLength / 2, angle, levels - 1) # recurse
        right(angle*2) # right by relative angle
        sidewaysTree(trunkLength / 2, angle, levels - 1) # recurse
        left(angle)
        backward(trunkLength) # move backward to the beginning
