from bank import BankAccount

# Bad example on purpose: both tests share one account, so test_b_withdraw
# only passes if test_a_deposit has already run.
shared_account = BankAccount(100)


def test_a_deposit():
    shared_account.deposit(50)
    assert shared_account.balance == 150


def test_b_withdraw():
    shared_account.withdraw(30)
    assert shared_account.balance == 120
