'''
Задача 2. Магия
Для одной игры необходимо реализовать механику магии, где при соединении
двух элементов получается новый. У нас есть четыре базовых элемента:
«Вода», «Воздух», «Огонь», «Земля». Из них получаются новые: «Шторм»,
«Пар», «Грязь», «Молния», «Пыль», «Лава».
Таблица преобразований:
● Вода + Воздух = Шторм;
● Вода + Огонь = Пар;
● Вода + Земля = Грязь;
● Воздух + Огонь = Молния;
● Воздух + Земля = Пыль;
● Огонь + Земля = Лава.
Напишите программу, которая реализует все эти элементы. Каждый элемент
необходимо организовать как отдельный класс. Если результат не определён,
то возвращается None.
Примечание: сложение объектов можно реализовывать через магический
метод __add__, вот пример использования:
class ExampleOne:
def __add__(self, other):
return ExampleTwo()
class ExampleTwo:
answer = 'сложили два класса и вывели'
first_example = ExampleOne()
second_example = ExampleTwo()
result = first_example + second_example
print(result.answer)
Дополнительно: придумайте свой элемент (или элементы) и реализуйте его
взаимодействие с остальными.
Подсказка № 1
Используйте магический метод __add__ для определения взаимодействия двух
элементов. Этот метод позволяет определить, что произойдет при сложении двух
объектов, и возвращает новый объект, если комбинация определена.
Подсказка № 2
Создайте отдельные классы для каждого базового элемента (Вода, Воздух, Огонь,
Земля) и производных элементов (Шторм, Пар, Грязь, Молния, Пыль, Лава). Это
поможет разделить логику обработки различных типов взаимодействий.
Подсказка № 3
Используйте проверку типа через isinstance внутри метода __add__ для определения,
с каким элементом происходит сложение. Это позволит точно определить результат
взаимодействия.
Подсказка № 4
Добавьте метод __str__ или атрибут answer для каждого производного элемента, чтобы
можно было легко выводить результат взаимодействия в виде строки.
Подсказка № 5
Перед созданием архива убедитесь, что исходный каталог существует, чтобы избежать
ошибок. Используйте os.path.isdir() для проверки существования каталога.
'''
class Element:
   def __add__(self, other):
      return None

class Water(Element):
   def __add__(self, other):
      if isinstance(other, Air):
         return Storm()
      elif isinstance(other, Fire):
         return Steam()
      elif isinstance(other, Earth):
         return Mud()
      return None

class Air(Element):
   def __add__(self, other):
      if isinstance(other, Water):
         return Storm()
      elif isinstance(other, Fire):
         return Lightning()
      elif isinstance(other, Earth):
         return Dust()
      return None

class Fire(Element):
   def __add__(self, other):
      if isinstance(other, Water):
         return Steam()
      elif isinstance(other, Air):
         return Lightning()
      elif isinstance(other, Earth):
         return Lava()
      return None

class Earth(Element):
   def __add__(self, other):
      if isinstance(other, Water):
         return Mud()
      elif isinstance(other, Air):
         return Dust()
      elif isinstance(other, Fire):
         return Lava()
      return None

class Storm(Element):
   answer = 'Шторм'

class Steam(Element):
   answer = 'Пар'

class Mud(Element):
   answer = 'Грязь'

class Lightning(Element):
   answer = 'Молния'

class Dust(Element):
   answer = 'Пыль'

class Lava(Element):
   answer = 'Лава'

# Пример использования
water = Water()
air = Air()
fire = Fire()
earth = Earth()

result = water + air
if result:
   print(result.answer)  # Вывод: Шторм

result = water + fire
if result:
   print(result.answer)  # Вывод: Пар

result = water + earth
if result:
   print(result.answer)  # Вывод: Грязь

result = air + fire
if result:
   print(result.answer)  # Вывод: Молния

result = air + earth
if result:
   print(result.answer)  # Вывод: Пыль

result = fire + earth
if result:
   print(result.answer)  # Вывод: Лава

#Этот код создает классы для каждого базового элемента и производных элементов. Метод __add__ определяет, что произойдет при сложении двух объектов, и возвращает новый объект, если комбинация определена. Если результат не определен, возвращается None.