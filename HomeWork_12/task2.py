'''
Задача 2. Класс с валидацией данных
Создайте класс Person, который имеет атрибуты name, age, и email. При
установке значения атрибута name, оно должно начинаться с заглавной буквы.
При установке значения атрибута age, оно должно быть целым числом в
диапазоне от 0 до 120. При установке значения атрибута email, оно должно
содержать символ @.
Подсказка № 1
Используйте метод __setattr__ для валидации установки атрибутов. Этот метод
позволяет вам перехватывать присвоение значений атрибутам класса, что удобно для
реализации проверки корректности значений.
Подсказка № 2
Проверьте, что значение атрибута name начинается с заглавной буквы и состоит
только из букв. Используйте методы строк isupper() и isalpha() для проверки
первой буквы и содержания строки.
Подсказка № 3
Проверьте, что значение атрибута age является целым числом в диапазоне от 0 до
120. Используйте isinstance() для проверки типа данных и логическое выражение
для проверки диапазона.
Подсказка № 4
Проверьте, что значение атрибута email содержит символ @. Для этого достаточно
проверить, присутствует ли символ @ в строке с помощью оператора in.
Подсказка № 5
Используйте метод super().__setattr__ для установки атрибутов после проверки. Это
позволит избежать рекурсии и правильно установить значение атрибута после
выполнения всех проверок.
'''

class Person:
   def __init__(self, name, age, email):
      self.name = name
      self.age = age
      self.email = email

   def __setattr__(self, name, value):
      if name == "name":
         if not value.istitle() or not value.replace(' ', '').isalpha():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
         elif name == "age":
            if not isinstance(value, int) or not (0 <= value <= 120):
               raise ValueError("Возраст должен быть целым числом в диапазоне от 0 до 120")
         elif name == "email":
            if '@' not in value:
               raise ValueError("Email должен содержать символ @")
      super().__setattr__(name, value)

   def __str__(self):
      return f"Person(name={self.name}, age={self.age}, email={self.email})"

# Пример использования
try:
   person = Person("Иван Иванов", 25, "ivan@example.com")
   print(person)

   person.name = "иван иванов"  # Это вызовет ошибку
except ValueError as e:
   print(e)

try:
   person.age = 130  # Это вызовет ошибку
except ValueError as e:
   print(e)

try:
   person.email = "ivanexample.com"  # Это вызовет ошибку
except ValueError as e:
   print(e)


'''
В этом коде:

1. Метод __setattr__ используется для проверки значений атрибутов перед их установкой.
2. Проверка для name убеждается, что значение начинается с заглавной буквы и состоит только из букв.
3. Проверка для age убеждается, что значение является целым числом в диапазоне от 0 до 120.
4. Проверка для email убеждается, что значение содержит символ @.
'''