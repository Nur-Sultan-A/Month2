#Dunder methods - magic methods double underscore
class Money:
    def __init__(self, amoutn=0):
        self.amount = amoutn

    def __str__(self):
        return f' экземпляр Money {self.amount}'

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        return Money(self.amount * other.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    #gt - greater than - self > other
    #ge - greater than or equal: self > other
    #lt - less than: self < other
    #le - less than or equal: self < other
    def __gt__(self, other):
        return self.amount > other.amount

igor_money = Money(100)
print(igor_money)
adilet_money = Money(250)
total1 = igor_money + adilet_money
print(total1)
print(total1 == adilet_money)
print(total1 > adilet_money)