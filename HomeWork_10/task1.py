'''
Задание 1. Отцы, матери и дети.
Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
● имя,
● возраст,
● список детей.
И он может:
● сообщить информацию о себе,
● успокоить ребёнка,
● покормить ребёнка.
У ребёнка есть:
● имя,
● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
● состояние спокойствия,
● состояние голода.
Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
и словарь состояний, и что-то поинтереснее.
Подсказка № 1
Используйте проверку на разницу в возрасте при добавлении ребёнка в список детей.
Это поможет убедиться, что разница в возрасте между родителем и ребёнком
составляет хотя бы 16 лет.
Подсказка № 2
Реализуйте методы feed() и calm() в классе Parent, чтобы они изменяли
соответствующие состояния ребёнка. Например, состояние голода можно представить
как логическое значение (True/False) или строку («голоден»/«сыт»).
Подсказка № 3
Используйте методы __str__() или __repr__() в классах Parent и Child, чтобы
предоставить более удобный вывод информации о них. Это улучшит читаемость кода,
когда объекты классов будут выводиться в консоль.
Подсказка № 4
Добавьте метод для вывода информации о детях родителя. Это позволит родителю
предоставить информацию о всех своих детях в одном месте, что упростит управление
объектами.
'''
class Child:
   def __init__(self, name, age):
      self.name = name
      self.age = age
      self.is_calm = True
      self.is_hungry = False

   def __str__(self):
      return f"Ребёнок: {self.name}, Возраст: {self.age}, Спокоен: {self.is_calm}, Голоден: {self.is_hungry}"

class Parent:
   def __init__(self, name, age):
      self.name = name
      self.age = age
      self.children = []

   def add_child(self, child):
      if self.age - child.age >= 16:
         self.children.append(child)
      else:
         print(f"Ошибка: разница в возрасте между {self.name} и {child.name} должна быть не менее 16 лет.")

   def feed(self, child):
      if child in self.children:
         child.is_hungry = False
         print(f"{child.name} теперь сыт.")
      else:
         print(f"{child.name} не является ребёнком {self.name}.")

   def calm(self, child):
      if child in self.children:
         child.is_calm = True
         print(f"{child.name} теперь спокоен.")
      else:
         print(f"{child.name} не является ребёнком {self.name}.")

   def __str__(self):
      return f"Родитель: {self.name}, Возраст: {self.age}, Дети: {[child.name for child in self.children]}"

   def children_info(self):
      for child in self.children:
         print(child)

# Пример использования
parent = Parent("Вася", 40)
child1 = Child("Петя", 20)
child2 = Child("Маша", 18)

parent.add_child(child1)
parent.add_child(child2)

print(parent)
parent.feed(child1)
parent.calm(child2)
parent.children_info()