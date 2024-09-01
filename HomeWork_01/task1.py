# Задание 1. Рамка
# Напишите программу, которая рисует прямоугольную рамку с помощью
# символьной графики. Для вертикальных линий используйте символ
# вертикального штриха (|), а для горизонтальных — дефис (-). Пусть ширину и
# высоту рамки определяет пользователь.

'''
Подсказка № 1
Используйте цикл for для создания строк рамки. Каждая итерация этого цикла будет
соответствовать одной строке.

Подсказка № 2
Внутри внешнего цикла используйте ещё один цикл for для создания символов в
строке. Каждая итерация этого цикла будет соответствовать одному символу в строке.
Подсказка № 3

Используйте условные выражения if для определения, какой символ выводить:
вертикальную линию (|), горизонтальную линию (-) или пробел ( ).

'''

# Пользователь определяет ширину и высоту рамки:

width = int(input('Введите ширину рамки  '))
height = int(input('Введите высоту рамки  '))

# width = 7  # Ширина прямоугольника
# height = 4  # Высота прямоугольника


#for i in range(height):
#   for j in range(width):
#      if i == 0 or i == height - 1 or j == 0 or j == width - 1: # условие создания рамки
#         print('-', end=' ') # условие печатания одного символа без перехода на новую строку
#      else:
#         print(' ', end=' ')
#   print()


for i in range(height):
   for j in range(width):
      if i == 0 or i == height - 1:  # Верхняя и нижняя границы
         if j == 0 or j == width - 1:
            print('|', end=' ')
         else:
            print('-', end=' ')
      elif j == 0 or j == width - 1:  # Левая и правая границы
         print('|', end=' ')
      else:
         print(' ', end=' ')
   print()  # Переход на новую строку после завершения внутреннего цикла

