# class is blueprint for object
class Computer:
    num_computers = 0
    ram = []
    #class atribute without self
    def __init__(self):
        Computer.num_computers += 1
        #define className.num_computers + 1 for every new instance
        ## Computer.ram.append(8)
        self.ram = [8]
        self.pc_name = 'PC'
        self.is_on = False
        self.is_charging = False
        self.mouseposX = 0.0
        self.mouseposY = 0.0
        #the state of an object
        self.primary_cpu = CPU()


class CPU:
    def __init__(self):
        self.bits64 = False
        self.gflops = 0.0
        self.clock_speed = 0
        self.company = ''

# instance
rob_computer = Computer()
paja_computer = Computer()

#modify atribut object in instance

rob_computer.pc_name = 'Rob PC'
paja_computer.pc_name = 'Paja PC'

rob_computer.is_on = True
paja_computer.is_on = False

both_on = rob_computer.is_on and paja_computer.is_on
# print(both_on)
# print(rob_computer.is_on)
# print(rob_computer.pc_name)

rob_computer.primary_cpu.bits64 = True
rob_computer.primary_cpu.gflops = 98.6

print(rob_computer.primary_cpu.gflops)

print(rob_computer == paja_computer)
#return False

# self.fur_color = 'yellow'
pc1 = Computer()
pc2 = Computer()
pc3 = Computer()

print(Computer.num_computers)
print(pc1.ram)
