class InsufficientFundsError(Exception):
    def __init__(self,balance, amount):
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return f'Невозможно снять {self.amount}, так как баланс банкомата {self.balance}'