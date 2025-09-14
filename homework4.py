class Vehicle:
    def start(self):
        print('vehicle starting')

class Car(Vehicle):
    def start(self):
        super().start()
        print('car starting')

class ElectricCar(Vehicle):
    def start(self):
        super().start()
        pass

class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print('tesla starting')

test = Tesla()
test.start()






