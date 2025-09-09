class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}. "
              f"Я {self.occupation}, родился {self.birth_date}. "
              f"Высшее образование: {'Есть' if self.higher_education else 'Нет'}.")


#Класс одногруппник
class Classmate(Person):
    def introduce(self):
        print(f"Я твой одногруппник, меня зовут {self.name}. "
              f"Учусь на {self.occupation}. "
              f"Дата рождения: {self.birth_date}.")


#Класс друг
class Friend(Person):
    def introduce(self):
        print(f"Привет, я {self.name}, твой друг и сын маминой подруги! "
              f"Работаю как {self.occupation}. "
              f"Высшее образование у меня {'есть' if self.higher_education else 'нет'}.")


#примеры
classmate1 = Classmate("Алия", "12.03.1880", "программиста", True)
classmate2 = Classmate("Нурбек", "05.07.2025", "экономиста", False)

friend1 = Friend("Эрмек", "01.01.2005", "бариста", False)
friend2 = Friend("Айжанбек", "10.09.2004", "дизайнер", True)

#делаем метод introduce у каждого
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()