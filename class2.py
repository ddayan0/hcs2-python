#class1.py
#Dennis Dayan
def line():
    print('------------------\n')

class Car:


    def __init__(self, year, make, model,):
        self.year = year
        self.make = make
        self.model = model
        self.odo_miles = 0
        self.gas_miles = 500
    def honk(self):
        return 'HOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKK'


    def registration(self):
        return 'Hello citizen, welcome to the MVC. Your cars information is that it was made in {} and it is a {} {} with {} miles.'.format(self.year, self.make, self.model, self.odo_miles)

    def drive(self, milesDriven):
        if (milesDriven > -1):
            if(self.gas_miles == 0):
                return 'The {} has no gas!'.format(self.model)
            #if gas_miles > MilesDriven and gas_miles < 500
            elif(self.gas_miles > milesDriven and milesDriven <= 500):
                self.odo_miles += milesDriven
                self.gas_miles -= milesDriven
                return 'Your mileage is now {} on your {} {}.'.format(self.odo_miles, self.make, self.model)
            else:
                #if we drive and run out of gas
                self.odo_miles += self.gas_miles
                print('The {} drove {} miles, but ran out of gas.'.format(self.model, self.gas_miles))
                self.gas_miles = 0
        else:
            print('EMPTY TANK')

    def fillUp(self):
        self.gas_miles = 500
        return 'Your ferrari 458 has been filled up and its gas tank now has a range of {} miles'.format(self.gas_miles)


porsche = Car(2016, 'Porsche', 'Carrera')
ferrari = Car(2016, 'Ferrari', 458)
mclaren = Car(2016, 'McLaren', 'P1')

print(porsche.model)
line()
print(porsche.honk())
line()
print(porsche.registration())
line()
print(porsche.drive(45))
line()
print(ferrari.model)
line()
print(ferrari.registration())
line()
print(ferrari.drive(90))
line()
print(mclaren.model)
line()
print(mclaren.registration())
line()
print(mclaren.drive(180))
line()
print(ferrari.drive(2000))
line()
print(ferrari.fillUp())

