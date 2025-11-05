class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number # Protected attribute
        self.__balance = balance # Private attribute

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        
account = BankAccount("12345", 500)
print("Initial Balance:", account.get_balance())

account.deposit(200)
print("After Deposit:", account.get_balance())

account.withdraw(100)
print("After Withdrawal:", account.get_balance())


        