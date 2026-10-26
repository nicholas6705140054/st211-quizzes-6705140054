from bank import BankAccount


def test_deposit():
    account = BankAccount(100)  # repeated setup
    account.deposit(50)
    assert account.balance == 150


def test_withdraw():
    account = BankAccount(100)  # repeated setup
    account.withdraw(30)
    assert account.balance == 70
