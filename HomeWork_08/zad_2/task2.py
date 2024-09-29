'''
Задача 2. Объединение данных из нескольких JSON файлов
Напишите скрипт, который объединяет данные из нескольких JSON файлов в
один. Каждый файл содержит список словарей, описывающих сотрудников
компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
содержать объединённые списки сотрудников из всех файлов.
Пример: У вас есть три файла employees1.json, employees2.json,
employees3.json. Нужно объединить их в один файл all_employees.json.
Подсказка № 1
Используйте функцию glob.glob() для поиска всех JSON файлов в указанной
директории.
Подсказка № 2
Откройте каждый JSON файл с помощью json.load() и добавьте данные в общий
список. Функция json.load() позволяет прочитать содержимое JSON файла и
преобразовать его в Python объект. Используйте list.extend() для объединения
данных.
Подсказка № 3
Сохраните объединенные данные в новый JSON файл с помощью json.dump(). После
объединения данных, используйте json.dump() для записи списка в новый JSON
файл.
'''
import glob
import json

def merge_json_files(directory, output_file):
# Ищем все JSON файлы в указанной директории
   json_files = glob.glob(f"{directory}/employees*.json")
   merged_data = []

   for file in json_files:
      try:
         with open(file, 'r') as f:
            data = json.load(f)
            merged_data.extend(data)
      except json.JSONDecodeError:
         print(f"Ошибка чтения JSON файла: {file}")

   with open(output_file, 'w') as f:
      json.dump(merged_data, f, indent=4)

if __name__ == "__main__":
   merge_json_files('HomeWork_08/zad_2', 'all_employees.json')
   
