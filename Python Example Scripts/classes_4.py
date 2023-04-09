

class Car:
    #define Class Attibutes
    manufacturer = 'Ford'

    #define Constructor Method
    def __init__(self, model, liter, year):
        #instance attributes
        self.model = model
        self.liter = liter
        self.year = year
    
    #define instance methods

    def start(self):
        print('this car can start')

    def stop(self):
        print('this car can stop')


#now create an instance/object of class car

car1 = Car('f-150', 3.4, 1990)
car2 = Car('Raptor', 2.8, 2005)

#lets access these objects/instances Class attributes which are common for all objects

print(car1.manufacturer)
print(car2.manufacturer)

#lets access these objects intance attributes

print(car1.model)
print(car2.model)

#lets access instance methods

print(car1.start())
print(car2.stop())