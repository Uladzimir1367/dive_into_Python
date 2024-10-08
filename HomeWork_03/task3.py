'''
Задача 3. Проверка палиндрома
Напишите программу, которая принимает строку и определяет, является ли она
палиндромом (читается одинаково с обеих сторон).
Подсказка № 1
После получения строки от пользователя, используйте метод lower() для
преобразования всех символов в нижний регистр. Это поможет игнорировать регистр
при проверке палиндрома.
Подсказка № 2
Создайте пустое множество odd_chars для хранения символов, которые встречаются
в строке нечетное количество раз. Это множество будет использоваться для проверки,
сколько символов встречаются нечетное количество раз.
Подсказка № 3
Для каждого символа в строке используйте операцию if char in odd_chars для
проверки, содержится ли символ в множестве. Если да, удалите его, иначе добавьте
его в множество.
Подсказка № 4
После обработки всех символов в строке, используйте len(odd_chars) для
определения размера множества. Если его размер не больше одного, строка может
быть палиндромом.
'''
"""
Шаги решения задачи:
1. Получение строки: Ввод строки от пользователя.
2. Преобразование в нижний регистр: Использование метода lower() для игнорирования регистра.
3. Создание пустого множества odd_chars.
4. Обработка каждого символа: Проверка каждого символа и обновление множества odd_chars.
5. Проверка размера множества: Определение, является ли строка палиндромом на основе размера множества.
"""

# Ввод строки от пользователя
input_str = input("Введите строку: ")

# Преобразование строки в нижний регистр
input_str = input_str.lower()

# Создание пустого множества для хранения символов с нечетным количеством вхождений
odd_chars = set()

# Обработка каждого символа в строке
for char in input_str:
   if char in odd_chars:
      odd_chars.remove(char)
   else:
      odd_chars.add(char)

# Проверка размера множества
if len(odd_chars) <= 1:
   print("Строка является палиндромом.")
else:
   print("Строка не является палиндромом.")

'''
Пояснение:
1. Ввод строки: Пользователь вводит строку.
2. Преобразование в нижний регистр: input_str.lower() преобразует все символы строки в нижний регистр.
3. Создание множества: odd_chars = set() создает пустое множество для хранения символов, которые встречаются нечетное количество раз.
4. Обработка символов: Цикл for char in input_str проходит по каждому символу строки. Если символ уже есть в множестве odd_chars, он удаляется, иначе добавляется.
5. Проверка множества: Если размер множества len(odd_chars) не больше одного, строка может быть палиндромом (т.е. все символы встречаются четное количество раз, кроме, возможно, одного).
'''
