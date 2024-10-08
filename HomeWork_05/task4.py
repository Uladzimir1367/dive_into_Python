'''
Задача 4. Генератор подстрок
Напишите генераторную функцию substrings(s), которая принимает строку
s и возвращает генератор всех возможных подстрок этой строки.
На вход подается строка abc
На выходе будут выведены обозначения:
a
ab
abc
b
bc
c
Подсказка № 1
Чтобы создать генератор подстрок, начните с определения всех возможных начальных
и конечных позиций для подстрок. Перебирайте начальные позиции, затем для каждой
начальной позиции перебирайте все возможные конечные позиции.
Подсказка № 2
Используйте два вложенных цикла для генерации всех подстрок. Внешний цикл будет
проходить по начальным позициям подстрок, а внутренний цикл будет проходить по
конечным позициям, начиная с текущей начальной позиции и до конца строки.
Подсказка № 3
Внутри вложенного цикла используйте оператор yield для возврата подстроки,
которая начинается на текущей начальной позиции и заканчивается на текущей
конечной позиции. Убедитесь, что конечная позиция не выходит за пределы строки.
'''

def substrings(s):
   length = len(s)
   for start in range(length):
      for end in range(start + 1, length + 1):
         yield s[start:end]

# Пример использования функции-генератора
s = "abc"
for substring in substrings(s):
   print(substring)
'''
Эта функция substrings(s) генерирует все возможные подстроки строки s. Внешний цикл перебирает начальные позиции подстрок, а внутренний цикл — конечные позиции, начиная с текущей начальной позиции и до конца строки. На каждой итерации внутреннего цикла функция возвращает подстроку с помощью оператора yield.
'''