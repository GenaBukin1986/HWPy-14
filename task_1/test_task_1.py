import pytest
from task_1 import BankAccount
from error_task_1 import InsufficientFundsError

@pytest.fixture
def data_test_1():
    return BankAccount()

@pytest.fixture
def data_test_3(data_test_1):
    data_test_1.deposit(1000)
    return data_test_1

@pytest.fixture
def data_test_4(data_test_3):
    data_test_3.withdraw(999)
    return data_test_3

@pytest.fixture
def data_test_2():
    return BankAccount(1000)



def test_1(data_test_1):
    assert data_test_1.get_balance() == 0

def test_2(data_test_2):
    assert data_test_2.get_balance() == 1000

def test_3(data_test_3):
    assert data_test_3.get_balance() == 1000

def test_4(data_test_4):
    assert data_test_4.get_balance() == 1

def test_5(data_test_1):
    with pytest.raises(InsufficientFundsError):
        data_test_1.withdraw(1000)

def test_6(data_test_1):
    with pytest.raises(ValueError):
        data_test_1.deposit(-1000)

if __name__ == '__main__':
    pytest.main(['-v'])