#cоздаем класс личности и
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

#тут я создал функцию представление что они из себя представляют
    def introduce(self):
        print('\nИнформация о пользователе'
              f'\nИмя: {self.name}'
              f'\nДень рождения: {self.birth_date}'
              f'\nПрофессия: {self.occupation}'
              f'\nВысшее образование: {"Есть" if self.higher_education else "Нет"}')

# примеры
p1 = Person("Игорь Препод", "2001-04-15", "Программист", True)
p2 = Person("Балабол", "1990-11-02", "Студентка", False)
p3 = Person("Баба яга", "1567-10-10", "MAgictriCK", False)

# Вызов метода introduce
p1.introduce()
p2.introduce()
p3.introduce()