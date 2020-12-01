import pyautogui
from random import randint

class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        
    def X(self):
        return self.X

    def Y(self):
        return self.Y
    
    def setX(self,x):
        self.X = x
    
width, height = pyautogui.size() # Screen size
actual = Point(0, 0) # Origin point
    
# quadrant I: 0 - width/2, 0 - height/2
# quadrant II: width/2 - width, 0 - height/2
# quadrant III: width/2 - width, height/2 - height
# quadrant IIII: 0 - width/2, height/2 - height

def isInQuadrant(point): # returns quadrant of point
    if (point.Y > height/2):
        if (point.X > width/2):
            return 2
        else:
            return 1
    elif (point.X > width/2):
        return 3
    else:
        return 4

def random():
    x = randint(1, round(0.95 * width)) # limit = 1, width * 0.95
    y = randint(1, round(0.95 * height)) # limit = 1, height
    t = randint(0, 5) # limit = 0, 5
    point = Point(x, y)
    if (isInQuadrant(actual) != isInQuadrant(point)): # change quadrant
        actual = Point(x, y) # update actual
        pyautogui.moveTo(x, y, t)
        random()
    else:
        random()

try:
    print("To stop the program, put the mouse in a corner of the screen")
    random()
except:
    print("You stopped the program")
    exit()
