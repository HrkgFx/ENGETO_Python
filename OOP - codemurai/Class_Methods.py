# class is blueprint for object
class Computer:
    def __init__(self):
        self.monitor_on = False
        self.cpu_on = False

    #define method
    def turn_on(self):
        self.monitor_on = True
        self.cpu_on = True

    #define another method
    def turn_off(self):
        self.monitor_on = False
        self.cpu_on = False

    def type_key(self, key):
        print (key)

rob_computer = Computer()
rob_computer.turn_on()
# monitor_on = True, cpu_on = True
rob_computer.turn_off()
# monitor_on = False, cpu_on = False


rob_computer.type_key('a')
Computer.type_key('x','a')


class Math:
    @staticmethod
    def circle_area(r):
        return 3.14 * r * r

radius = 3
area = Math.circle_area(radius)
print(area)
