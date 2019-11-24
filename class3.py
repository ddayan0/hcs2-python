#class3.py
#dennis dayan
#sorry about the returns, I just hate how it prints "none" at the end. hope ya understand
def line():
    print('-------------------------------\n')

class Robot:
    population = 0
    robotlist = []
    def __init__(self, name):
        self.name = name
        self.batteryPower = 100
        Robot.population += 1
        self.robot_num = Robot.population
        Robot.robotlist.append(self.name)
        print('YOU HAVE BEEN IDENTIFIED AS ROBOT {} WITH ROBOT NUMBER {}, INITIALIZING!'.format(self.name, self.robot_num))
    def charge_robot(self):
        if self.batteryPower == 100:
            self.batteryPower = 100
            return 'YOUR BATTERY IS AT {} PERCENT, NUMBER {} '.format(self.batteryPower, self.robot_num)
        if self.batteryPower == 75:
            self.batteryPower = 100
            return 'YOUR BATTERY IS AT {} PERCENT, NUMBER {} '.format(self.batteryPower, self.robot_num)
        if self.batteryPower < 75:
            self.batteryPower + 25
            return 'YOUR BATTERY IS AT {} PERCENT, NUMBER {} '.format(self.batteryPower, self.robot_num)
    def is_robot_alive(self):
        if self.batteryPower == 0:
            print('ROBOT {}, YOU ARE OFFLINE!'.format(self.robot_num))
        if self.batteryPower < 25:
            print('ROBOT {}, CONNECT TO A CHARGING STATION IMMEDIATELY!'.format(self.robot_num))
        else:
            print('ROBOT {}, YOUR BATTERY IS NOW AT {} PERCENT. YOU ARE PROPERLY FUNCTIONING!'.format(self.robot_num, self.batteryPower))
    def do_robot_things(self, action):
        print('{}:'.format(self.name), end= '')
        for i in range(1, 11):
            print('{}'.format(action.upper()), end = ' ')
        print()
        self.batteryPower -= 10
        self.is_robot_alive()

    @classmethod
    def robot_roll_call(self):
        for i in range(len(Robot.robotlist)):
            if(i < len(Robot.robotlist)-1):
                print(Robot.robotlist[i], end=', ')
            else:
                print(Robot.robotlist[i])







robot1 = Robot('dennis')
robot2 = Robot('Godzilla')
robot3 = Robot('R2D2')
robot4 = Robot('Mark Zuckerberg')
robot5 = Robot('Steve Jobs')
line()
print(robot1.charge_robot())
print(robot2.charge_robot())
print(robot3.charge_robot())
print(robot4.charge_robot())
print(robot5.charge_robot())
line()
(robot1.is_robot_alive())
(robot2.is_robot_alive())
(robot3.is_robot_alive())
(robot4.is_robot_alive())
(robot5.is_robot_alive())
line()
robot1.do_robot_things('go to bed')
line()
robot2.do_robot_things('make food')
line()
robot3.do_robot_things('do homework')
line()
robot4.do_robot_things('steal ur data')
line()
robot5.do_robot_things('upcharge laptops')
line()

#List Below
Robot.robot_roll_call()

