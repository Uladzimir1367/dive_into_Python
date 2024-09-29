'''
Задача 4. Агрегирование данных из CSV файла
Напишите скрипт, который считывает данные из CSV файла, содержащего
информацию о продажах (название продукта, количество, цена за единицу), и
подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
новом CSV файле.
Пример: Из файла sales.csv нужно создать файл total_sales.csv, где для каждого
продукта будет указана общая выручка.
Подсказка № 1
Используйте csv.DictReader для чтения данных из исходного CSV файла.
csv.DictReader позволяет читать строки CSV файла как словари, где ключи
соответствуют заголовкам столбцов.
Подсказка № 2
Создайте словарь для хранения выручки по каждому продукту. Используйте продукт в
качестве ключа и выручку в качестве значения. Убедитесь, что добавляете выручку при
встрече одинакового продукта.
Подсказка № 3
Используйте csv.DictWriter для записи данных в новый CSV файл. Запишите итоговые
данные в новый файл, указывая заголовки столбцов и записывая итоговую выручку
для каждого продукта.
Подсказка № 4
Преобразуйте данные в числовые типы для корректного вычисления выручки.
Убедитесь, что данные из CSV преобразованы в целые или вещественные числа,
чтобы корректно производить арифметические операции.
'''
import csv

def calculate_total_sales(input_file, output_file):
   sales_data = {}

# Чтение данных из исходного CSV файла
   with open(input_file, 'r', encoding='utf-8') as f:
      reader = csv.DictReader(f)
      for row in reader:
         product = row['product']
         quantity = int(row['quantity'])
         price = float(row['price'])
         revenue = quantity * price

   if product in sales_data:
      sales_data[product] += revenue
   else:
      sales_data[product] = revenue

# Запись итоговых данных в новый CSV файл
   with open(output_file, 'w', newline='', encoding='utf-8') as f:
      writer = csv.DictWriter(f, fieldnames=['product', 'total_revenue'])
      writer.writeheader()
      for product, total_revenue in sales_data.items():
         writer.writerow({'product': product, 'total_revenue': total_revenue})

# Пример использования функции
calculate_total_sales('sales.csv', 'total_sales.csv')
