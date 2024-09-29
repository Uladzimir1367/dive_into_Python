'''
Задание 1. Работа с основными данными
Напишите функцию, которая получает на вход директорию и рекурсивно обходит
её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
pickle. Для дочерних объектов указывайте родительскую директорию. Для
каждого объекта укажите файл это или директория. Для файлов сохраните его
размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
задания функций пакет для работы с файлами разных форматов.
Подсказка № 1
Для рекурсивного обхода используйте функцию os.walk(). Эта функция генерирует
имена файлов и директорий в указанной директории и ее поддиректориях. Внутри
цикла можно разделять файлы и директории и собирать информацию о них.
Подсказка № 2
Используйте os.path.getsize() для определения размера файла. Эта функция
возвращает размер файла в байтах. Для директорий вы можете использовать
рекурсивный обход для вычисления общего размера всех вложенных файлов.
Подсказка № 3
Для сбора информации о каждом объекте создайте словарь. Словарь должен
содержать такие ключи, как 'name', 'path', 'type', 'size', и 'parent'.
Используйте os.path.basename() для получения имени родительской директории.
Подсказка № 4
Сохраняйте данные в разные форматы с помощью соответствующих библиотек.
Используйте json.dump() для JSON, csv.DictWriter() для CSV и
pickle.dump() для Pickle.
'''
import os
import json
import csv
import pickle

def get_size(path):
   if os.path.isfile(path):
      return os.path.getsize(path)
   elif os.path.isdir(path):
      total_size = 0
      for dirpath, _, filenames in os.walk(path):
         for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(full_path)
   return total_size

def traverse_directory(directory):
   result = []
   for root, dirs, files in os.walk(directory):
      for name in dirs + files:
         path = os.path.join(root, name)
         is_dir = os.path.isdir(path)
         size = get_size(path)
         parent = os.path.basename(root)
         result.append({
            'name': name,
            'path': path,
            'type': "directory" if is_dir else "file",
            'size': size,
            'parent': parent
         })
   return result

def save_to_json(data, filename):
   with open(filename, 'w') as json_file:
      json.dump(data, json_file, indent=4)

def save_to_csv(data, filename):
   with open(filename, 'w', newline='') as csv_file:
      writer = csv.DictWriter(csv_file, fieldnames=['name', 'path', 'type', 'size', 'parent'])
      writer.writeheader()
      writer.writerows(data)

def save_to_pickle(data, filename):
   with open(filename, 'wb') as pickle_file:
      pickle.dump(data, pickle_file)

# Пример использования функций
def main(directory):
   data = traverse_directory(directory)

   save_to_json(data, 'directory_info.json')
   save_to_csv(data, 'directory_info.csv')
   save_to_pickle(data, 'directory_info.pkl')

if __name__ == "__main__":
   main('HomeWork_08')