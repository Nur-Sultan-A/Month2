#OOП 1: Основы ООП, Создание первых классов, Атрибуты и Методы классов, Принцип ООП - Наследование.
class Car:
    #init = инициализатор
  def __init__(self, color, model):
      self.color = color
      self.model = model

  def drive_to_location(self, location):
       print(f"Car {self.model} is driving to {location}")

car_honda = Car('black', 'honda')
print(car_honda)
car_bmw = Car('white', 'bmw')
print(car_bmw)
car_bmw.drive_to_location('Bishkek')
print(f'Car color: {car_honda.color} \nmodel: {car_honda.model}')
car_bmw.color = 'red'
print(f'Car color: {car_bmw.color} \nmodel: {car_bmw.model}')
# print(type(car_honda))
# print(type(23123132))
# print(type('siufg'))