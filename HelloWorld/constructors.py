
# a Contrcutor is a fuction that is called at the time of object creation

class Point:
    #lets define a contructor which will be called at the time of object creations
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # lets define other methods of this class    
    def move(self):   #self is reff to current object
        print ("move")
    def draw(self):   #self is reff to current object
        print ("move")


# lets create an object

point = Point(10,20)
#point.x = 10
print (point.x)