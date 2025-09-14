class Animal:
    def speak(self):
        print('animal speaking')


class Dog(Animal):
    def speak(self):
        print('gav')


class Cat(Animal):
    def speak(self):
        print('meow')


class Catdog (Dog, Cat):
    def speak(self):
        print('gav ,meow')
        super().speak()# тот самый __mro__ метод то есть решение diamon problem

kotopes = Catdog()
kotopes.speak()
print(Catdog.__mro__)#mro- method resolution order- метод решения порядка
