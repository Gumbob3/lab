import pytest
import account
from account import Account

def test_init(self):
    #This is a test for my init method in account.py
    assert Account.get_name(self) == "Name"
    assert Account.get_balance(self) == 0

def test_deposit(self):
    #This is a test for my deposit method in account.py
    Account.deposit(self, 15)
    assert Account.get_balance(self) == 15

def test_withdraw(self):
    #This is a test for my withdraw method in account.py
    Account.deposit(self, 50)
    Account.withdraw(self, 10)
    assert Account.get_balance(self) == 40
