#OOП 2: Другие принципы ООП - Инкапсуляция, Полиморфизм
class Car:
    #init = инициализатор
  def __init__(self, color, model):
      self.color = color
      self.model = model

  def drive_to_location(self, location):
       print(f"Car {self.model} is driving to {location}")

class Bus(Car):
    def drive_to_location(self, location):
        print(f"Bus {self.model} is driving to {location}")

bus_40 = Bus('invisible',40)
bus_40.drive_to_location('Bishkek')
print(bus_40.color)
