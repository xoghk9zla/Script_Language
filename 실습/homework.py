class BankAccount:
    def __init__(self, balance, name, number):
        self.balance = balance
        self.name = name
        self.number = number
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self. balance += amount
    def __str__(self):
        return "잔액: " + str(self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, balance, name, number, interest_rate):
        super().__init__(balance, name, number)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += self.balance * self.interest_rate
    def __str__(self):
        return super().__str__() + ", 계좌번호: " + str(self.number)

class CheckingAccount(BankAccount):
    def __init__(self, balance, name, number, withdraw_charge):
        super().__init__(balance, name, number)
        self.withdraw_charge = withdraw_charge
    def withdraw(self, amount):
        super().withdraw(amount + self.withdraw_charge)
    def __str__(self):
        return super().__str__()

s = SavingsAccount(100000, "ㅇㅇㅇ", "9381932319", 0.03)
s.add_interest()
print(s)

c = CheckingAccount(300000, "xxx", "312312432", 0.01)
c.withdraw(10000)
print(c)