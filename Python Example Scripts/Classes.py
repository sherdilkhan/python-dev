
# Int Char(ASCII) FLoat Bool
# String (array of characters)
#----------------------
#List (array of strings)
#Distionaries (definitions of new names)
# but for more complex parts, lets assume a shopping cart. this can not be presented by any of the above
# so we use classes to define new types.
# lets define a new type "Point". This new type is going to have methods to work with points.

from msilib.schema import SelfReg

numbers = [1,2,3]

# pascal naming convention for classes with first char upper case
class Point:
    def move(self): # class method def
        print ("move") 
    def draw (self): # class method def
        print ("draw") 
     
# creat an object

point1 = Point()
point1.draw()
point1.x = 10 # object attribute (we can do this with constructor,see contructors.py file for this)
print (point1.x)

# lets creat another object

point2 = Point()
point2.move()
point2.x =20 # object attribute (we can do this with constructor, see constructor.py file for this)
print (point2.x)




