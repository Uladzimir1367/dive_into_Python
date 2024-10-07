'''
Задание 1. Работа с данными студентов
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только
букв. Если ФИО не соответствует условию, выведите:
ФИО должно состоять только из букв и начинаться с заглавной буквы
○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
Предмет {Название предмета} не найден
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до
100). В противном случае выведите:
Оценка должна быть целым числом от 2 до 5
Результат теста должен быть целым числом от 0 до 100
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по
оценкам всех предметов вместе взятых.
Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана
следующая информация.
Математика,Физика,История,Литература
Создайте класс Student, который будет представлять студента и его успехи по
предметам. Класс должен иметь следующие методы:
Атрибуты класса:
name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в
качестве ключей и информацию об оценках и результатах тестов для каждого предмета в
виде словаря.
Магические методы (Dunder-методы):
__init__(self, name, subjects_file): Конструктор класса. Принимает имя студента
и файл с предметами и их результатами. Инициализирует атрибуты name и subjects и
вызывает метод load_subjects для загрузки предметов из файла.
__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута
name. Убеждается, что name начинается с заглавной буквы и состоит только из букв.
__getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок
и результатов тестов) по их именам.
__str__(self): Возвращает строковое представление студента, включая имя и список
предметов.
Студент: Иван Иванов
Предметы: Математика, История
Методы класса:
load_subjects(self, subjects_file): Загружает предметы из файла CSV.
Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут
subjects.
add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
Убеждается, что оценка является целым числом от 2 до 5.
add_test_score(self, subject, test_score): Добавляет результат теста по
заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.
get_average_test_score(self, subject): Возвращает средний балл по тестам для
заданного предмета.
get_average_grade(self): Возвращает средний балл по всем предметам.
Пример
На входе:
student = Student("Иван Иванов", "subjects.csv")
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)
student.add_grade("История", 5)
student.add_test_score("История", 92)
average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")
average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике:
{average_test_score}")
print(student)
На выходе:
Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История
Подсказка № 1
Используйте модуль csv для чтения данных из файла CSV. Этот модуль позволяет
легко читать и обрабатывать строки из CSV файлов. Используйте csv.reader для
чтения содержимого файла и создания списка предметов.
Подсказка № 2
В методе __setattr__ используйте проверки для валидации ФИО. Проверяйте, что ФИО
начинается с заглавной буквы и состоит только из букв, чтобы избежать неверного
ввода данных.
Подсказка № 3
Используйте метод __getattr__ для обработки запросов к атрибутам предметов. Этот
метод позволяет динамически возвращать значения атрибутов, если они существуют в
словаре предметов, или выбрасывать исключение, если нет.
Подсказка № 4
Добавьте проверки значений оценок и результатов тестов в методах add_grade и
add_test_score. Убедитесь, что оценки находятся в пределах от 2 до 5, а результаты
тестов — от 0 до 100, чтобы предотвратить некорректный ввод данных.
Подсказка № 5
В методе get_average_grade и get_average_test_score используйте списковые
включения для сбора всех оценок и результатов тестов. Это позволит легко вычислить
среднее значение по всем предметам или конкретному предмету
'''

import csv

class NameDescriptor:
   def __get__(self, instance, owner):
      return instance._name

   def __set__(self, instance, value):
      if not value.istitle() or not value.replace(' ', '').isalpha():
         raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
      instance._name = value

class Student:
   name = NameDescriptor()

   def __init__(self, name, subjects_file):
      self.name = name
      self.subjects = {}
      self.load_subjects(subjects_file)

   def load_subjects(self, subjects_file):
      with open(subjects_file, newline='', encoding='utf-8') as csvfile:
         reader = csv.reader(csvfile)
         for row in reader:
            for subject in row:
               self.subjects[subject.strip()] = {'grades': [], 'test_scores': []}

   def add_grade(self, subject, grade):
      if subject not in self.subjects:
         raise ValueError(f"Предмет {subject} не найден")
      if not (2 <= grade <= 5):
         raise ValueError("Оценка должна быть целым числом от 2 до 5")
      self.subjects[subject]['grades'].append(grade)

   def add_test_score(self, subject, test_score):
      if subject not in self.subjects:
         raise ValueError(f"Предмет {subject} не найден")
      if not (0 <= test_score <= 100):
         raise ValueError("Результат теста должен быть целым числом от 0 до 100")
      self.subjects[subject]['test_scores'].append(test_score)

   def get_average_test_score(self, subject):
      if subject not in self.subjects:
         raise ValueError(f"Предмет {subject} не найден")
         scores = self.subjects[subject]['test_scores']
      return sum(scores) / len(scores) if scores else 0

   def get_average_grade(self):
      total_grades = []
      for subject in self.subjects.values():
         total_grades.extend(subject['grades'])
      return sum(total_grades) / len(total_grades) if total_grades else 0

   def __str__(self):
      subjects_list = ', '.join(self.subjects.keys())
      return f"Студент: {self.name}\nПредметы: {subjects_list}"

# Пример использования
student = Student("Иван Иванов", "subjects.csv")
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)
student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)


#Этот код создает класс Student с дескриптором для проверки ФИО, методами для загрузки предметов из файла CSV, добавления оценок и результатов тестов, а также вычисления среднего балла по тестам и оценкам. 
