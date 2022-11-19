class Account:

    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        success = True
        if amount <= 0:
            success = False
            return success
        else:
            self.__account_balance = self.__account_balance + amount
            success = True
        return success

    def withdraw(self, amount):
        success = True
        if amount <= 0:
            success = False
            return success
        elif amount < self.__account_balance:
            success = False
            return success
        else:
            self.__account_balance = self.__account_balance - amount
            success = True
        return success

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name


