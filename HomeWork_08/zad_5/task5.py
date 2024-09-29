'''
Задача 5. Конвертация  JSON в  изменением структуры данных
Напишите скрипт, который считывает данные из JSON файла и сохраняет их в
CSV файл с другой структурой. 

'''
import json
import csv

def json_to_csv_with_structure_change(json_file, csv_file):
# Чтение данных из JSON файла
   with open(json_file, 'r', encoding='utf-8') as f:
      data = json.load(f)

# Подготовка данных для новой структуры
      transformed_data = []
      for student in data:
         name = student['name']
         age = student['age']
         for grade in student['grades']:
            transformed_data.append({
               'name': name,
               'age': age,
               'grade': grade
            })

# Запись данных в CSV файл
   with open(csv_file, 'w', newline='', encoding='utf-8') as f:
      writer = csv.DictWriter(f, fieldnames=['name', 'age', 'grade'])
      writer.writeheader()
      writer.writerows(transformed_data)

# Пример использования функции
json_to_csv_with_structure_change('students.json', 'students_transformed.csv')

'''
Объяснение:
1. Чтение данных из JSON файла: Используется json.load() для загрузки данных из JSON файла в виде списка словарей.
2. Преобразование структуры данных: Для каждого студента создается новая запись для каждой его оценки, включающая имя, возраст и оценку.
3. Запись данных в CSV файл: Используется csv.DictWriter для записи данных в CSV файл с новой структурой. Заголовки столбцов указываются как name, age и grade.
'''