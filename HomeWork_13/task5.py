'''
Задача 5. Валидатор Пользовательских Данных
Создайте класс User, который содержит атрибуты name, email, и age.
Необходимо убедиться, что:
● Имя состоит из хотя бы двух слов, каждое из которых начинается с
заглавной буквы.
● Электронная почта содержит символ @ и точку . после @.
● Возраст — это положительное целое число, не меньше 0 и не больше
120.
Создайте пользовательские исключения для каждой из этих проверок:
● NameError: Если имя не соответствует формату.
● EmailError: Если электронная почта не соответствует формату.
● AgeError: Если возраст вне допустимого диапазона.
Подсказка № 1
Создайте пользовательские исключения. Определите три класса исключений
(NameError, EmailError, AgeError), наследующие от базового класса Exception.
Установите сообщения об ошибках в конструкторах этих классов, чтобы указать, какие
именно ошибки произошли.
Подсказка № 2
Используйте свойства (геттеры и сеттеры) в классе User для контроля установки
значений атрибутов name, email, и age. Это позволяет выполнять проверки перед
присваиванием значений.
Подсказка № 3
Убедитесь, что имя состоит из хотя бы двух слов, каждое из которых начинается с
заглавной буквы. Используйте метод split() для разделения имени на слова и
проверьте первый символ каждого слова с помощью isupper().
Подсказка № 4
Убедитесь, что электронная почта содержит символ @ и точку . после символа @.
Используйте метод split('@') для разделения строки и проверяйте наличие точки в
части после @.
Подсказка № 5
Убедитесь, что возраст является целым числом в пределах от 0 до 120. Используйте
функцию isinstance() для проверки типа данных и операторы сравнения для
проверки диапазона.
'''

class NameError(Exception):
   def __init__(self, message="Имя должно состоять из двух слов, каждое из которых начинается с заглавной буквы."):
      self.message = message
      super().__init__(self.message)

class EmailError(Exception):
   def __init__(self, message="Электронная почта должна содержать символ @ и точку после @."):
      self.message = message
      super().__init__(self.message)

class AgeError(Exception):
   def __init__(self, message="Возраст должен быть положительным целым числом от 0 до 120."):
      self.message = message
      super().__init__(self.message)

class User:
   def __init__(self, name, email, age):
      self.name = name
      self.email = email
      self.age = age

   @property
   def name(self):
      return self._name

   @name.setter
   def name(self, value):
      if not self.validate_name(value):
         raise NameError()
      self._name = value

   @property
   def email(self):
      return self._email

   @email.setter
   def email(self, value):
      if not self.validate_email(value):
         raise EmailError()
      self._email = value

   @property
   def age(self):
      return self._age

   @age.setter
   def age(self, value):
      if not self.validate_age(value):
         raise AgeError()
      self._age = value

   @staticmethod  
   def validate_name(name):
      words = name.split()
      return len(words) >= 2 and all(word[0].isupper() for word in words)

   @staticmethod
   def validate_email(email):
      parts = email.split('@')
      return len(parts) == 2 and '.' in parts[1]

   @staticmethod
   def validate_age(age):
      return isinstance(age, int) and 0 <= age <= 120

# Пример использования
try:
   user = User("Иван Иванов", "ivan.ivanov@example.com", 30)
   print(f"Пользователь создан: {user.name}, {user.email}, {user.age}")
except (NameError, EmailError, AgeError) as e:
   print(e)

'''
Этот код включает:

1.Классы пользовательских исключений NameError, EmailError и AgeError.
2.Класс User с атрибутами name, email и age, а также соответствующими геттерами и сеттерами для проверки значений.
3.Статические методы для валидации имени, электронной почты и возраста.
'''