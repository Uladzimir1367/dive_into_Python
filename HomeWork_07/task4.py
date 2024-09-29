'''
Задача 4. Поиск файлов по расширению
Напишите функцию, которая находит и перечисляет все файлы с заданным
расширением в указанном каталоге и всех его подкаталогах. Функция должна
принимать путь к каталогу и расширение файла.
Подсказка № 1
Используйте os.walk() для рекурсивного обхода указанного каталога. Это позволяет
вам обрабатывать все файлы в текущем каталоге и во всех его подкаталогах.
Подсказка № 2
Используйте метод str.endswith() для проверки, имеет ли имя файла указанное
расширение. Это поможет вам отфильтровать файлы по заданному типу.
Подсказка № 3
Используйте os.path.join() для объединения пути к каталогу и имени файла,
чтобы получить полный путь к файлу. Это поможет корректно обрабатывать файлы в
разных каталогах
'''

import os

def find_files_by_extension(directory, extension):
# Проверяем, существует ли указанный каталог
   if not os.path.isdir(directory):
      print(f"Каталог {directory} не существует.")
      return

# Список для хранения найденных файлов
   found_files = []

# Обходим все файлы и подпапки в указанном каталоге
   for root, dirs, files in os.walk(directory):
      for file in files:
# Проверяем, имеет ли файл указанное расширение
         if file.endswith(extension):
# Полный путь к файлу
            full_path = os.path.join(root, file)
            found_files.append(full_path)

# Выводим найденные файлы
   for file in found_files:
      print(file)

# Пример использования функции
find_files_by_extension('/path/to/directory', '.txt')

'''
Пояснения:
1. Проверка существования каталога: Используем os.path.isdir() для проверки, существует ли указанный каталог.
2. Создание списка для хранения найденных файлов: Инициализируем пустой список found_files.
3. Обход всех файлов и подпапок: Используем os.walk() для рекурсивного обхода всех каталогов и файлов в указанном каталоге.
4. Проверка расширения файла: Используем метод str.endswith() для проверки, имеет ли имя файла указанное расширение.
5. Получение полного пути к файлу: Используем os.path.join() для объединения пути к каталогу и имени файла.
6. Вывод найденных файлов: Перебираем список found_files и выводим каждый найденный файл.
'''