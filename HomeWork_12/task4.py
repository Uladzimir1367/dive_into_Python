'''
Задача 4. Класс с контролем цены и количества
Создайте класс Product с атрибутами name, price, и quantity. price должен
быть положительным числом, а quantity неотрицательным целым числом. При
попытке установить price или quantity, должен производиться контроль
значений.
Подсказка № 1
Используйте метод __setattr__ для контроля значений атрибутов. Переопределите
метод __setattr__, чтобы проверять, что price является положительным числом, а
quantity — неотрицательным целым числом, прежде чем устанавливать значение
атрибутов.
Подсказка № 2
Проверьте тип и значение для price. Убедитесь, что price является либо целым
числом, либо числом с плавающей точкой, и что оно больше нуля.
Подсказка № 3
Проверьте тип и значение для quantity. Убедитесь, что quantity является целым
числом и не отрицательным.
Подсказка № 4
Используйте метод super().__setattr__ для установки атрибутов после проверки.
Вызовите метод super().__setattr__ для фактического присвоения значений
атрибутам после проверки.
'''

class Product:
   def __init__(self, name, price, quantity):
      self.name = name
      self.price = price
      self.quantity = quantity

   def __setattr__(self, name, value):
      if name == "price":
         if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError("Цена должна быть положительным числом")
      elif name == "quantity":
         if not (isinstance(value, int) and value >= 0):
            raise ValueError("Количество должно быть неотрицательным целым числом")
      super().__setattr__(name, value)

   def __str__(self):
      return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

# Пример использования
try:
   product = Product("Laptop", 1500.0, 10)
   print(product)

   product.price = -100  # Это вызовет ошибку
except ValueError as e:
   print(e)

try:
   product.quantity = -5  # Это вызовет ошибку
except ValueError as e:
   print(e)

'''
В этом коде:

1. Метод __setattr__ используется для проверки значений атрибутов перед их установкой.
2. Проверка для price убеждается, что значение является либо целым числом, либо числом с плавающей точкой, и что оно больше нуля.
3. Проверка для quantity убеждается, что значение является целым числом и не отрицательным.
4. Метод __str__ возвращает строковое представление экземпляра Product.

При попытке установить некорректные значения для price или quantity, будет выброшено исключение ValueError. 
'''