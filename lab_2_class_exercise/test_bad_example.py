from bank import BankAccount


# Bad example on purpose: three actions in one test. If it fails you cannot
# tell whether deposit or withdraw broke. Prefer one action per test.
def test_everything_at_once():
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    account.deposit(10)
    assert account.balance == 130
