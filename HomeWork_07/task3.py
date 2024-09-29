'''
Задача 3. Удаление старых файлов
Напишите скрипт, который удаляет файлы в указанном каталоге, которые не
изменялись более заданного количества дней. Скрипт должен принимать путь к
каталогу и количество дней.
Подсказка № 1
Используйте time.time() для получения текущего времени в секундах с начала
эпохи (01.01.1970). Это поможет вам определить, сколько времени прошло с
последнего изменения файлов.
Подсказка № 2
Преобразуйте количество дней в секунды для сравнения. Умножьте количество дней
на 86400 (количество секунд в одном дне), чтобы получить пороговое значение
времени.
Подсказка № 3
Используйте os.walk() для рекурсивного обхода всех каталогов и файлов в
указанном каталоге. Это позволит вам проверить каждый файл, независимо от уровня
вложенности.
Подсказка № 4
Для получения времени последнего изменения файла используйте
os.path.getmtime(). Сравните это время с пороговым значением, чтобы
определить, нужно ли удалить файл.
Подсказка № 5
Для удаления файлов используйте os.remove(). Убедитесь, что файл действительно
нужно удалить, чтобы избежать случайного удаления важных данных.
'''
import os
import time

def delete_old_files(directory, days):
# Проверяем, существует ли указанный каталог
   if not os.path.isdir(directory):
      print(f"Каталог {directory} не существует.")
   return

# Текущее время в секундах с начала эпохи
   current_time = time.time()
# Пороговое значение времени в секундах
   threshold_time = current_time - (days * 86400)

# Обходим все файлы и подпапки в указанном каталоге
   for root, dirs, files in os.walk(directory):
      for file in files:
         file_path = os.path.join(root, file)
# Время последнего изменения файла
         file_mtime = os.path.getmtime(file_path)
# Проверяем, нужно ли удалить файл
      if file_mtime < threshold_time:
         os.remove(file_path)
      print(f"Удален файл: {file_path}")

# Пример использования функции
delete_old_files('/path/to/directory', 30)
'''
Пояснения:
1. Проверка существования каталога: Используем os.path.isdir() для проверки, существует ли указанный каталог.
2. Получение текущего времени: Используем time.time() для получения текущего времени в секундах с начала эпохи.
3. Преобразование дней в секунды: Умножаем количество дней на 86400 (количество секунд в одном дне) для получения порогового значения времени.
4. Обход всех файлов и подпапок: Используем os.walk() для рекурсивного обхода всех каталогов и файлов в указанном каталоге.
5. Получение времени последнего изменения файла: Используем os.path.getmtime() для получения времени последнего изменения файла.
6. Удаление файлов: Используем os.remove() для удаления файлов, которые не изменялись более заданного количества дней.
'''