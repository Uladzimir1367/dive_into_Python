'''
Задача 2. Недоделка
Вы пришли на работу в компанию по разработке игр, целевая аудитория —
дети и их родители. У предыдущего программиста было задание сделать две
игры в одном приложении, чтобы пользователь мог выбирать одну из них.
Однако программист, на место которого вы пришли, перед увольнением не
успел выполнить эту задачу и оставил только небольшой шаблон проекта.
Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай
число».
Правила игры «Камень, ножницы, бумага»: программа запрашивает у
пользователя строку и выводит, победил он или проиграл. Камень бьёт
ножницы, ножницы режут бумагу, бумага кроет камень.
Правила игры «Угадай число»: программа запрашивает у пользователя число
до тех пор, пока он не отгадает загаданное.
'''
'''
def rock_paper_scissors():
   #Здесь будет игра "Камень, ножницы, бумага"

def guess_the_number():
   # Здесь будет игра "Угадай число"
   
def mainMenu():
   # Здесь главное меню игры
   
mainMenu():
   pass

Подсказка № 1
Реализуйте функцию для игры "Камень, ножницы, бумага". Начните с запроса выбора
игрока. Убедитесь, что ваш код правильно обрабатывает ввод пользователя и
проверяет его на допустимые значения. Затем, используя логические условия,
определите победителя, исходя из выбранного игроком и компьютером варианта.
Подсказка № 2
Создайте цикл для игры "Угадай число". В этой игре, создайте бесконечный цикл,
который будет продолжаться до тех пор, пока игрок не угадает загаданное число.
Внутри цикла запрашивайте ввод числа у пользователя и проверяйте его на
соответствие загаданному числу.
Подсказка № 3
Определите структуру главного меню. В main_menu предоставьте пользователю выбор
между двумя играми и опцией выхода. Используйте условные операторы для
определения, какую функцию вызывать в зависимости от выбора пользовател
'''
import random

def rock_paper_scissors():
   choices = ["камень", "ножницы", "бумага"]
   computer_choice = random.choice(choices)
   user_choice = input("Выберите: камень, ножницы или бумага: ").lower()

   if user_choice not in choices:
      print("Неверный выбор. Попробуйте снова.")
      return

   print(f"Компьютер выбрал: {computer_choice}")

   if user_choice == computer_choice:
      print("Ничья!")
   elif (user_choice == "камень" and computer_choice == "ножницы") or \
      (user_choice == "ножницы" and computer_choice == "бумага") or \
      (user_choice == "бумага" and computer_choice == "камень"):
      print("Вы выиграли!")
   else:
      print("Вы проиграли!")

def guess_the_number():
   number_to_guess = random.randint(1, 100)
   guess = None

   while guess != number_to_guess:
      guess = int(input("Угадайте число от 1 до 100: "))

      if guess < number_to_guess:
         print("Загаданное число больше.")
      elif guess > number_to_guess:
         print("Загаданное число меньше.")
      else:
         print("Поздравляю! Вы угадали число.")

def main_menu():
   while True:
      print("\nГлавное меню")
      print("1. Камень, ножницы, бумага")
      print("2. Угадай число")
      print("3. Выход")
      choice = input("Выберите игру (1/2) или выход (3): ")

      if choice == "1":
         rock_paper_scissors()
      elif choice == "2":
         guess_the_number()
      elif choice == "3":
         print("До свидания!")
         break
      else:
         print("Неверный выбор. Попробуйте снова.")

# Запуск главного меню
main_menu()
