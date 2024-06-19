import threading
import time


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Пополнение баланса на {amount}. Текущий баланс {self.balance}')

    def withdrow(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Вывод средств. Снято {amount}. Текущий баланс {self.balance}')
            else:
                print(f'Средств на счету недостаточно для снятия {amount}. Текущий баланс {self.balance}')

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdrow_task(account, amount):
    for _ in range(11):
        account.withdrow(amount)


account = BankAccount(balance=1000)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdrow_thread = threading.Thread(target=withdrow_task, args=(account, 175))

deposit_thread.start()
withdrow_thread.start()

deposit_thread.join()
withdrow_thread.join()
