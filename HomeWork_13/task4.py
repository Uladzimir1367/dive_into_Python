'''
Задача 4. Счетчик Очков в Игрe
Создайте класс GameScore для отслеживания очков игрока. В этом классе
должны быть методы для добавления и уменьшения очков. Однако:
● Очки не могут быть отрицательными.
● Если игрок пытается добавить больше очков, чем 1000, должно быть
выброшено исключение ScoreLimitExceededError.
Создайте пользовательское исключение ScoreLimitExceededError.
Подсказка № 1
Создайте пользовательское исключение. Определите класс
ScoreLimitExceededError, который наследует от Exception. В конструкторе этого
класса задайте сообщение об ошибке, которое будет отображаться при выбросе
исключения.
Подсказка № 2
Реализуйте метод add_score. В методе add_score класса GameScore проверьте, не
превышает ли новая сумма очков допустимый лимит (1000). Если превышает,
выбросите исключение ScoreLimitExceededError.
Подсказка № 3
Реализуйте метод subtract_score. В методе subtract_score проверьте, чтобы после
вычитания очков не образовался отрицательный результат. Если это произойдет,
выбросите стандартное исключение ValueError с соответствующим сообщением.
Подсказка № 4
В основном блоке программы используйте конструкцию try-except для обработки
исключений, выбрасываемых методами add_score и subtract_score. Выведите
соответствующее сообщение об ошибке, чтобы пользователь понял, что произошло.
'''

class ScoreLimitExceededError(Exception):
   def __init__(self, message="Превышен лимит очков!"):
      self.message = message
      super().__init__(self.message)

class GameScore:
   def __init__(self):
      self.score = 0

   def add_score(self, points):
      if self.score + points > 1000:
         raise ScoreLimitExceededError()
         self.score += points

   def subtract_score(self, points):
      if self.score - points < 0:
         raise ValueError("Очки не могут быть отрицательными!")
         self.score -= points

   def get_score(self):
      return self.score

# Основной блок программы
if __name__ == "__main__":
   game_score = GameScore()

while True:
   print(f"Текущий счет: {game_score.get_score()}")
   action = input("Выберите действие (add/subtract/exit): ").strip().lower()

   if action == "add":
      try:
         points = int(input("Введите количество очков для добавления: "))
         game_score.add_score(points)
      except ScoreLimitExceededError as e:
         print(e)
      except ValueError:
         print("Пожалуйста, введите корректное число.")
   elif action == "subtract":
      try:
         points = int(input("Введите количество очков для вычитания: "))
         game_score.subtract_score(points)
      except ValueError as e:
         print(e)
   elif action == "exit":
      break
   else:
      print("Неверное действие. Пожалуйста, выберите add, subtract или exit.")


'''
Этот код включает:

1. Класс ScoreLimitExceededError, который наследует от Exception и задает сообщение об ошибке.
2. Класс GameScore с методами add_score, subtract_score и get_score.
3. Основной блок программы, который позволяет пользователю добавлять или вычитать очки и обрабатывает исключения.
'''