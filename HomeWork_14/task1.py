'''
Задание 1. Тестирование класса с использованием pytest
Напишите класс BankAccount, который управляет балансом счета. Он должен
поддерживать следующие методы:
● deposit(amount): добавляет указанную сумму к балансу.
● withdraw(amount): снимает указанную сумму с баланса, если достаточно
средств.
● get_balance(): возвращает текущий баланс счета.
При попытке снять больше средств, чем доступно на счете, должно
выбрасываться исключение InsufficientFundsError. Напишите как минимум
5 тестов для проверки работы классов и его методов.
Подсказка № 1
Проверьте, что начальный баланс создаваемого объекта BankAccount корректен,
используя значение, переданное в конструкторе. Убедитесь, что баланс
инициализируется правильно при создании объекта.
Подсказка № 2
Проверьте, что метод deposit корректно добавляет указанную сумму к текущему
балансу. Убедитесь, что сумма депозита положительна и увеличивает баланс на
ожидаемое значение.
Подсказка № 3
Убедитесь, что метод withdraw корректно уменьшает баланс на указанную сумму,
если на счету достаточно средств. Проверьте правильность работы метода при
различных значениях суммы.
Подсказка № 4
Убедитесь, что метод withdraw корректно выбрасывает исключение
InsufficientFundsError, когда пытаются снять больше средств, чем доступно на
счету. Используйте pytest.raises для проверки этого поведения.
Подсказка № 5
Проверьте, что при создании объекта BankAccount без указания начального баланса,
баланс инициализируется как 0. Это поможет убедиться в правильности работы
конструктора с дефолтными значениями.
'''

# Класс BankAccount и исключение InsufficientFundsError
class InsufficientFundsError(Exception):
   pass

class BankAccount:
   def __init__(self, initial_balance=0):
      self.balance = initial_balance

   def deposit(self, amount):
      if amount <= 0:
         raise ValueError("Deposit amount must be positive")
         self.balance += amount

   def withdraw(self, amount):
      if amount > self.balance:
         raise InsufficientFundsError("Insufficient funds")
         self.balance -= amount

   def get_balance(self):
      return self.balance

# Тесты с использованием pytest
import pytest

def test_initial_balance():
   account = BankAccount(100)
   assert account.get_balance() == 100

def test_initial_balance_default():
   account = BankAccount()
   assert account.get_balance() == 0

def test_deposit():
   account = BankAccount(100)
   account.deposit(50)
   assert account.get_balance() == 150

def test_withdraw():
   account = BankAccount(100)
   account.withdraw(50)
   assert account.get_balance() == 50

def test_withdraw_insufficient_funds():
   account = BankAccount(100)
   with pytest.raises(InsufficientFundsError):
      account.withdraw(150)

def test_deposit_negative_amount():
   account = BankAccount(100)
   with pytest.raises(ValueError):
      account.deposit(-50)

'''
Объяснение тестов
1. test_initial_balance: Проверяет, что начальный баланс корректен при создании объекта с указанным значением.
2. test_initial_balance_default: Проверяет, что начальный баланс равен 0, если не указано начальное значение.
3. test_deposit: Проверяет, что метод deposit корректно добавляет сумму к балансу.
4. test_withdraw: Проверяет, что метод withdraw корректно уменьшает баланс при достаточном количестве средств.
5. test_withdraw_insufficient_funds: Проверяет, что метод withdraw выбрасывает исключение InsufficientFundsError, если средств недостаточно.
6. test_deposit_negative_amount: Проверяет, что метод deposit выбрасывает исключение ValueError, если сумма депозита отрицательная.
'''