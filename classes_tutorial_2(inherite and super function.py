
class Car:  #parent class for Cars
    def __init__(self,make,color, hp, torque):
        self.make = make
        self.color = color
        self.hp = hp
        self.torque = torque  
class IC_Car(Car):   #this class is only for mechanical or IC engine car
    def __init__(self, make, color, hp, torque, liters, revo): 
        self.liters = liters
        self.revo = revo 
        super(IC_Car, self).__init__(make, color, hp ,torque)
        #class also needs the super() function to inherit the functionality from the parent class, 
        #otherwise, the child’s constructor method overrides the inheritance of the parent’s __init__ method

            
class E_Car(Car):    #this class is only for electric car
    def __init__(self,charge_time, OneCharge_km):
        self.charge_time = charge_time
        self.OneCharge_km = OneCharge_km

mcar1 = IC_Car('toyota', 'white', 550, 599, 2.4,9000)

print(mcar1.color)
print(mcar1.revo)
print(mcar1.liters)