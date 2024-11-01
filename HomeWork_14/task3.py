'''
Задача 3. Тестирование класса с использованием doctest
Напишите класс Rectangle, который управляет прямоугольником. Класс должен
поддерживать следующие методы:
● set_dimensions(width, height): устанавливает ширину и высоту
прямоугольника.
● get_area(): возвращает площадь прямоугольника.
● get_perimeter(): возвращает периметр прямоугольника.
Напишите 3 теста с помощью doctest.
Подсказка № 1
Убедитесь, что при создании объекта Rectangle с заданными шириной и высотой,
методы get_area и get_perimeter возвращают правильные значения.
Подсказка № 2
После установки новых размеров с помощью set_dimensions, убедитесь, что методы
get_area и get_perimeter обновляются корректно.
Подсказка № 3
Убедитесь, что метод set_dimensions выбрасывает исключение ValueError, если
переданы отрицательные значения для ширины или высоты.
Подсказка № 4
Убедитесь, что метод set_dimensions правильно обрабатывает нулевые значения.
Для нулевых значений площадь и периметр должны быть корректными (площадь
будет 0).
'''

class Rectangle:
   def __init__(self, width, height):
      '''
      Sets the dimensions of the rectangle.

      >>> rect = Rectangle(2, 3)
      >>> rect.set_dimensions(4, 5)
      >>> rect.width
      4
      >>> rect.height
      5
      >>> rect.set_dimensions(-1, 5)
      Traceback (most recent call last):
      ...
      ValueError: Width and height must be non-negative
      '''
      
      if width < 0 or height < 0:
         raise ValueError("Width and height must be non-negative")
      self.width = width
      self.height = height

   def set_dimensions(self, width, height):

      if width < 0 or height < 0:
         raise ValueError("Width and height must be non-negative")
      self.width = width
      self.height = height

   def get_area(self):
      """
      Returns the area of the rectangle.

      >>> rect = Rectangle(2, 3)
      >>> rect.get_area()
      6
      >>> rect.set_dimensions(4, 5)
      >>> rect.get_area()
      20
      """
      return self.width * self.height

   def get_perimeter(self):
      """
      Returns the perimeter of the rectangle.

      >>> rect = Rectangle(2, 3)
      >>> rect.get_perimeter()
      10
      >>> rect.set_dimensions(4, 5)
      >>> rect.get_perimeter()
      18
      """
      return 2 * (self.width + self.height)

if __name__ == "__main__":
   import doctest
   doctest.testmod()

'''
Объяснение тестов
1.set_dimensions: Проверяет, что метод корректно устанавливает новые размеры прямоугольника и выбрасывает исключение ValueError при отрицательных значениях.
2.get_area: Проверяет, что метод возвращает правильную площадь прямоугольника после установки начальных и новых размеров.
3.get_perimeter: Проверяет, что метод возвращает правильный периметр прямоугольника после установки начальных и новых размеров.

'''

