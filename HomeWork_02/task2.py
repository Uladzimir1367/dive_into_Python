'''
Задание 2. Преобразование числа в шестнадцатеричное
представление
Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление. Функцию hex используйте для
проверки своего результата.

Подсказка № 1
Для преобразования числа в шестнадцатеричное представление нужно сначала
определить символы, которые будут использоваться для представления цифр в этой
системе. В шестнадцатеричной системе используются цифры от 0 до 9 и буквы от A до
F.

Подсказка № 2
Обработайте случай, когда число равно 0. В этом случае шестнадцатеричное
представление числа всегда будет '0'.

Подсказка № 3
Учтите, что функция должна правильно обрабатывать отрицательные числа. Сначала
сохраните информацию о том, является ли число отрицательным, а затем
преобразуйте число в положительное для удобства работы.

Подсказка № 4
Создайте цикл, который будет последовательно делить число на 16 и записывать
остаток от деления в строку, представляющую шестнадцатеричное число. Добавляйте
соответствующий символ к результату.

Подсказка № 5
После завершения преобразования добавьте префикс '-' для отрицательных чисел.
Верните строковое представление числа в шестнадцатеричной системе.
'''

# Запрос пользователя на ввод числа
number = int(input('Введите целое число =    '))

# Определяем символы для цифр в 16 системе

hex_digits = "0123456789ABCDEF"


if number == 0:
   hex_string = '0'
else:
   is_negativ = number < 0
   if is_negativ:
      number = - number
   hex_string = " "
   while number > 0:
      remainder = number % 16
      hex_string = hex_digits[remainder] + hex_string
      number //= 16
         
   if is_negativ:
      hex_string = "-" + hex_string
         
print(hex_string) 
        

