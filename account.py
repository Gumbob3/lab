class Account:

    def __init__(self, name: str):
        '''
        This is an init function to set the default values for each account object
        :param name: This is the name of the account
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: int):
        '''
        This is a deposit function to deposit an amount to an account

        :param amount: This is the amount to be deposited
        :return: Returns whether the deposit was successful or not
        '''
        if amount <= 0:
            success = False
            return success
        else:
            self.__account_balance = self.__account_balance + amount
            success = True
        return success

    def withdraw(self, amount: int):
        '''
        This is a withdraw function to withdraw an amount from an account

        :param amount: This is the amount to be withdrawn
        :return: Returns whether the withdrawal was successful or not
        '''
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
        '''
        This is a function to get the balance of an account
        :return: Returns the balance of the account
        '''
        return self.__account_balance

    def get_name(self):
        '''
        This is a function to get the name of an account
        :return: Returns the balance of the account
        '''
        return self.__account_name

