
# ДЗ №2 (2-месяц)
# 1. Создать класс Person с атрибутами fullname, age, is_married
# class Person:
#     def __init__(self, fullname, age, is_married):

# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(
            f"Толук аты жөнү: {self.fullname}, жашы: {self.age}, үйбүлөлүк абалы: {self.is_married} "
        )

person = Person("Palanchaev Tukuncho", 20, "Boidok")
person.introduce_myself()


# 3. Создать класс Student наследовать его от класса Person и дополнить его методом average_value который запрашивал бы словарь, где ключ это название урока, а значение - оценка. Этот метод должен подсчитывать среднюю оценку ученика по всем предметам.

# class Student(Person):
#     def __init__(self, fullname, age, is_married):
#         Person.__init__(fullname, age, is_married)
#     def average_value(Student):
    
    

# 4. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience=0):
        Person.__init__(self,fullname, age, is_married)
        self.experience = experience
Kishi=Teacher ("Otkurbekov Konurbai", 22, "ui-buloluu",10)
Kishi.introduce_myself()
print(f"Стажы: {Kishi.experience}")


# 5. Добавить в класс Teacher атрибут класса salary


class Teacher(Person):
    def __init__(self, fullname, age, is_married,salary=0 ):
        Person.__init__(self,fullname, age, is_married)
        self.salary = salary
akcha=Teacher ("Otkurbekov Konurbai", 22, "ui-buloluu", 50000)
akcha.introduce_myself()
print(f"Айлык акы: {akcha.salary}")



# 6. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 3000 за каждый год опыта.



# 7. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату



# 8. Создать объект студента и распечатать всю информацию о нем и вывести среднюю оценку