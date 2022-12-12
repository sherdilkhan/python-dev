

#define machine class with machines data

class machine:
    def __init__(self, name, maker, mfg, type):
        self.name = name
        self.maker = maker
        self.mfg = mfg
        self.type = type
    def get_maker(self):
        return self.maker


class plant:
    def __init__(self, plant_name, max_machines):
        self.plant_name = plant_name
        self.max_machines = max_machines
        self.machines = []

    def add_machine(self,machine):
        if len(self.machines) < self.max_machines:
            self.machines.append(machine)
            return True
        False

        
mc1 = machine('dc650', 'toshiba', 2009, 'plc') #creat object mc1 for class machine
mc2 = machine('dc800', 'toshiba', 2008, 'plc')
mc3 = machine('dc150', 'kdk', 2002, 'plc')

plant1 = plant('dc', 10)
plant1.add_machine(mc1)
plant1.add_machine(mc2)
plant1.add_machine(mc3)



print (mc1.get_maker())
print (mc3.get_maker())

print (plant1.machines[2].name)