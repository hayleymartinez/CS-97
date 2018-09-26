from turtle import *

def regularNGon(n, sideLength):
    """Draws a regular polygon.

    Arguments:
    n - the number of sides
    sideLength - the length of each side
    """
    r = n
    return helper(n, sideLength, r)
    

def helper(n, sideLength, r):
    angle = 180 - (n - 2) * 180 / n
    if r == 0:
        return
    else:
        return forward(sideLength), left(angle), helper(n, sideLength, r-1)


def archSpiral(initialLen, increment, angle, n):
    """Draws an Archimedean spiral.
    Arguments:
    initialLen - the length of the first line segment
    increment - the amount to increment the length for the next segment
    angle - the angle to turn after each segment is drawn
    n - the number of segments to draw
    """
    if n == 0:
        return 
    else:
        return forward(initialLen), left(angle), archSpiral(initialLen + increment, increment, angle, n-1) 


def logSpiral(initialLen, percentIncrease, angle, n):
    """Draws an logarithmic spiral.

    Arguments:
    initialLen - the length of the first line segment
    percentIncrease - the percentage to increase the length for the next segment
    angle - the angle to turn after each segment is drawn
    n - the number of segments to draw
    """
    if n == 0:
        return 
    else:
        return forward(initialLen), left(angle), logSpiral(initialLen * ( 1 + (percentIncrease / 100)), percentIncrease, angle, n-1) 
