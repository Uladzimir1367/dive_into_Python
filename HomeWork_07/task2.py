'''
Задача 2. Создание архива каталога
Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
должен включать все файлы и подпапки исходного каталога.
Подсказка № 1
Используйте функцию os.walk() для обхода всех файлов и подпапок в исходном
каталоге. Это функция возвращает корневую папку, список директорий и список
файлов в каждом корневом каталоге.
Подсказка № 2
Для создания архива используйте zipfile.ZipFile() с режимом 'w' для записи.
Также передайте параметр zipfile.ZIP_DEFLATED, чтобы применить сжатие к
файлам в архиве.
Подсказка № 3
Чтобы сохранить структуру каталогов в архиве, используйте функцию
os.path.relpath(), чтобы добавить файлы в архив с путями относительно
исходного каталога.
Подсказка № 4
Для получения полного пути к файлу используйте os.path.join(root, file), где
root - это текущая корневая папка, а file - это имя файла.
Подсказка № 5
Перед созданием архива убедитесь, что исходный каталог существует, чтобы избежать
ошибок. Используйте os.path.isdir() для проверки существования каталога.
'''
import os
import zipfile

def zip_directory(src_directory, output_zip):
# Ensure the output directory exists
   os.makedirs(os.path.dirname(output_zip), exist_ok=True)

# Create the zip archive
   with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
# Walk through all files and subfolders in the source directory
      for root, dirs, files in os.walk(src_directory):
         for file in files:
# Full path to the file
            full_path = os.path.join(root, file)
# Path to the file relative to the source directory
            rel_path = os.path.relpath(full_path, src_directory)
# Add the file to the archive
            zipf.write(full_path, rel_path)
            print(f"Added {full_path} as {rel_path}")

# Example usage of the function
zip_directory('/path/to/src_directory', '/path/to/output.zip')

'''
Пояснения:
1.Проверка существования каталога: Используем os.path.isdir() для проверки, существует ли исходный каталог.
2.Создание zip-архива: Используем zipfile.ZipFile() с режимом 'w' для записи и параметром zipfile.ZIP_DEFLATED для сжатия файлов.
3.Обход всех файлов и подпапок: Используем os.walk() для обхода всех файлов и подпапок в исходном каталоге.
4.Получение полного пути к файлу: Используем os.path.join(root, file) для получения полного пути к файлу.
5.Сохранение структуры каталогов: Используем os.path.relpath() для добавления файлов в архив с путями относительно исходного каталога.
'''