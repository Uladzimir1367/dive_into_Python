'''
 Задача 3. Планирование задач
 Напишите функцию, которая принимает количество дней от текущей даты и
 возвращает дату, которая наступит через указанное количество дней. Дополнительно,
 выведите эту дату в формате YYYY-MM-DD.
 Подсказка № 1
 Используйте from datetime import datetime, timedelta, чтобы получить
 доступ к текущей дате и времени, а также к функции для добавления или вычитания
 дней.
 Подсказка № 2
 Вызовите datetime.now() для получения текущей даты и времени в виде объекта
 datetime.
 Подсказка № 3
 Создайте объект timedelta, который представляет собой интервал времени, а затем
 добавьте его к текущей дате для получения даты в будущем.
 Подсказка № 4
 Примените метод strftime() для преобразования объекта datetime в строку в
 формате YYYY-MM-DD.
'''

from datetime import datetime, timedelta

def get_future_date(days):
# Получаем текущую дату и время
   now = datetime.now()

# Создаем объект timedelta с указанным количеством дней
   future_date = now + timedelta(days=days)

# Форматируем дату в строку в формате YYYY-MM-DD
   formatted_date = future_date.strftime('%Y-%m-%d')

   return formatted_date

# Пример использования функции
days = 10
future_date = get_future_date(days)
print(f"Дата через {days} дней: {future_date}")

# Этот скрипт вычисляет дату, которая наступит через указанное количество дней от текущей даты, и выводит ее в формате YYYY-MM-DD.