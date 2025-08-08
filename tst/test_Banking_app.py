import pytest
from src.Banking_app import BankAccount

@pytest.fixture()
def user_account():
    return BankAccount(100)

def test_for_deposit(user_account):
    #user_account = BankAccount(100)
    user_account.deposit(50)
    result = user_account.get_balance()
    assert result == 150

def test_for_withdraw(user_account):
    #user_account = BankAccount(100)
    user_account.withdraw(50)
    result = user_account.get_balance()
    assert result == 50


