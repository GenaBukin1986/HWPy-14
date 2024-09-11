# Задание 1. Тестирование класса с использованием pytest
# Напишите класс BankAccount, который управляет балансом счета. Он должен
# поддерживать следующие методы:
# ● deposit(amount): добавляет указанную сумму к балансу.
# ● withdraw(amount): снимает указанную сумму с баланса, если достаточно
# средств.
# ● get_balance(): возвращает текущий баланс счета.
# При попытке снять больше средств, чем доступно на счете, должно
# выбрасываться исключение InsufficientFundsError.
# Напишите как минимум
# 5 тестов для проверки работы классов и его методов.
from task_1.error_task_1 import InsufficientFundsError


class BankAccount:
    def __init__(self, balance: int | float = 0):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Нельзя внести сумму равную или меньше нуля")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance, amount)
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
