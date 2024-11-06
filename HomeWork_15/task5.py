'''
Задача5.Запуск из командной строки
 Напишите код, который запускается из командной строки и получает на вход путь
до директории на ПК. Соберите информацию о содержимом в виде объектов
namedtuple. Каждый объект хранит: имя файла без расширения или название
каталога, расширение, если это файл, флаг каталога, название родительского
каталога. В процессе сбора сохраните данные в текстовый файл используя
логирование.
Подсказка № 1
Используйте функцию os.path.join() для правильного построения путей к файлам
и каталогам в зависимости от операционной системы.
Подсказка № 2
Используйте os.path.isdir() для проверки, является ли указанный путь
директорией перед тем как пытаться получить его содержимое.
Подсказка № 3
Используйте os.path.splitext() для разделения имени файла на основную часть
и расширение, где расширение можно очистить от начальной точки.
Подсказка № 4
Используйте logging.basicConfig() для настройки логирования, указав уровень
логирования и формат сообщений.
Подсказка № 5
Определите namedtuple для хранения информации о файлах и каталогах, что
позволяет легко управлять структурой данных и логированием.
'''

import os
import logging
from collections import namedtuple
import argparse

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Определение namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])

def collect_directory_info(directory):
   directory_info = []

# Проверка, является ли путь директорией
   if not os.path.isdir(directory):
      logging.error(f"Указанный путь не является директорией: {directory}")
   return directory_info

# Обход содержимого директории
   for root, dirs, files in os.walk(directory):
      parent_dir = os.path.basename(root)

# Обработка каталогов
   for dir_name in dirs:
      info = FileInfo(name=dir_name, extension='', is_dir=True, parent_dir=parent_dir)
      directory_info.append(info)
      logging.info(f"Каталог: {info}")

# Обработка файлов
   for file_name in files:
      name, extension = os.path.splitext(file_name)
      info = FileInfo(name=name, extension=extension.lstrip('.'), is_dir=False, parent_dir=parent_dir)
      directory_info.append(info)
      logging.info(f"Файл: {info}")

   return directory_info

def main():
# Создание парсера аргументов командной строки
   parser = argparse.ArgumentParser(description='Сбор информации о содержимом директории')
   parser.add_argument('directory', type=str, help='Путь до директории')

# Парсинг аргументов
   args = parser.parse_args()

# Сбор информации о директории
   directory_info = collect_directory_info(args.directory)

# Вывод информации (опционально)
   for info in directory_info:
      print(info)

if __name__ == '__main__':
   main()

'''
Этот скрипт выполняет следующие действия:

1.Настраивает логирование для записи информации в файл directory_info.log.
2.Определяет namedtuple для хранения информации о файлах и каталогах.
3.Использует функцию os.walk() для обхода содержимого директории.
4.Собирает информацию о каждом файле и каталоге, записывая её в лог и добавляя в список.
5.Принимает путь до директории в качестве аргумента командной строки.

Запуск скрипта - python task5.py /path/to/directory
 
'''