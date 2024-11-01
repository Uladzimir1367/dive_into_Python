'''
Задача 2. Тестирование класса с использованием unittest
Напишите класс Library, который управляет книгами. Класс должен поддерживать
следующие методы:
● add_book(title): добавляет книгу в библиотеку.
● remove_book(title): удаляет книгу из библиотеки.
● list_books(): возвращает список всех книг в библиотеке.
При попытке удалить книгу, которая не существует, должно выбрасываться исключение
BookNotFoundError. Для тестирования используйте unitest.
Подсказка № 1
Убедитесь, что метод add_book корректно добавляет книги в библиотеку. Для этого
добавьте книгу и проверьте, что она присутствует в списке всех книг.
Подсказка № 2
Проверьте, что метод remove_book корректно удаляет книгу из библиотеки. Добавьте
книгу, удалите ее и убедитесь, что она больше не присутствует в списке.
Подсказка № 3
Убедитесь, что метод remove_book корректно выбрасывает исключение
BookNotFoundError, если пытаетесь удалить книгу, которой нет в библиотеке.
Подсказка № 4
Проверьте, что метод list_books возвращает правильный список книг после
выполнения нескольких операций добавления и удаления книг.
'''

# Класс Library и исключение BookNotFoundError
class BookNotFoundError(Exception):
   pass

class Library:
   def __init__(self):
      self.books = []

   def add_book(self, title):
      self.books.append(title)

   def remove_book(self, title):
      if title not in self.books:
         raise BookNotFoundError(f"Book '{title}' not found in the library")
         self.books.remove(title)

   def list_books(self):
      return self.books

# Тесты с использованием unittest
import unittest

class TestLibrary(unittest.TestCase):

   def test_add_book(self):
      library = Library()
      library.add_book("The Great Gatsby")
      self.assertIn("The Great Gatsby", library.list_books())

   def test_remove_book(self):
      library = Library()
      library.add_book("1984")
      library.remove_book("1984")
      self.assertNotIn("1984", library.list_books())

   def test_remove_book_not_found(self):
      library = Library()
      with self.assertRaises(BookNotFoundError):
         library.remove_book("Nonexistent Book")

   def test_list_books(self):
      library = Library()
      library.add_book("To Kill a Mockingbird")
      library.add_book("Pride and Prejudice")
      library.remove_book("To Kill a Mockingbird")
      self.assertEqual(library.list_books(), ["Pride and Prejudice"])

   def test_initial_books_list(self):
      library = Library()
      self.assertEqual(library.list_books(), [])

if __name__ == '__main__':
   unittest.main()

'''
Объяснение тестов
1. test_add_book: Проверяет, что метод add_book корректно добавляет книгу в библиотеку.
2. test_remove_book: Проверяет, что метод remove_book корректно удаляет книгу из библиотеки.
3. test_remove_book_not_found: Проверяет, что метод remove_book выбрасывает исключение BookNotFoundError, если книга не найдена.
4. test_list_books: Проверяет, что метод list_books возвращает правильный список книг после добавления и удаления книг.
5. test_initial_books_list: Проверяет, что начальный список книг пуст при создании объекта Library.
'''
