class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}. "
              f"Моя профессия {self.occupation}. "
              f"Дата рождения: {self.birth_date}. "
              f"У меня {'есть' if self.higher_education else 'нет'} высшее образование.")


# Класс одногруппник
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия {self.occupation}. "
              f"Я учился с директором geeks в группе {self.group}. "
              f"У меня {'есть' if self.higher_education else 'нет'} высшее образование.")


# Класс друг
class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. "
              f"У меня {'есть' if self.higher_education else 'нет'} высшее образование.")


# Примеры
cl1 = Classmate("биба", "10.12.2015", "слуга народа", True, "901-A")
cl1.introduce()

fr1 = Friend("боба", "2.02.900", "владелец народа", False, "спать")
fr1.introduce()