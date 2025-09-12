#Магические, статичные, классовые методы в классах, множественное наследование.
#Полиморфизм
class Car:
  def drive(self):
    print("Driving")

class Bus(Car):
  def drive(self):
    print("Driving a bus")

class Truck(Car):
  def drive(self):
    print("Driving a truck")

cars = [Car(), Bus(), Truck()]
for car in cars:
  car.drive()
# Driving, Driving a bus, Driving a truck


#Инкапсуляция
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # публичное (видно всем)
        self.__balance = balance    # приватное (спрятано)

    def deposit(self, amount):      # метод пополнения
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):     # метод снятия
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):          # метод посмотреть баланс
        return self.__balance


# Создаём счёт
acc = BankAccount("Айгуль", 1000)

print(acc.owner)          # Можно напрямую: Айгуль
print(acc.get_balance())  # Через метод: 1000

acc.deposit(500)
print(acc.get_balance())  # 1500

acc.withdraw(200)
print(acc.get_balance())  # 1300

# Прямой доступ запрещён:
# print(acc.__balance)   # Ошибка! Баланс скрыт

