'''
Задача 3. Агрегирование данных из CSV файла
Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
файл. JSON файл содержит данные о продуктах (название, цена, количество на
складе). В CSV файле каждая строка должна соответствовать одному продукту.
Пример: Из файла products.json нужно создать products.csv.
Подсказка № 1
Используйте json.load() для чтения данных из JSON файла. Функция json.load()
позволяет загрузить данные из JSON файла в виде Python объекта, например, списка
словарей.
Подсказка № 2
Используйте csv.DictWriter для записи данных в CSV файл. Функция
csv.DictWriter позволяет записывать данные в CSV файл, где каждый словарь из
списка становится одной строкой в CSV.
Подсказка № 3
Обеспечьте правильное управление строками в CSV файле. При записи в CSV файл
используйте параметр newline='' в open(), чтобы избежать дополнительных пустых
строк между записями на Windows.
'''
import json
import csv

def json_to_csv(json_file, csv_file):
# Чтение данных из JSON файла
   with open(json_file, 'r', encoding='utf-8') as f:
      data = json.load(f)

# Запись данных в CSV файл
   with open(csv_file, 'w', newline='', encoding='utf-8') as f:
      writer = csv.DictWriter(f, fieldnames=['name', 'price', 'quantity'])
      writer.writeheader()
      writer.writerows(data)

# Пример использования функции
json_to_csv('products.json', 'products.csv')