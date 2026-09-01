from calculator import add, subtract, divide
import pytest

@pytest.fixture
def params():
    a = 10
    b = 5
    
    print("Testcase Started")
    yield a,b
    print("Testcase Ended")
    
def test_add_positive_number(params):
    assert add(params[0],params[1]) == 15
        
def test_subtract_mix_numbers():
    assert subtract(-1, 2) == -3

@pytest.mark.can_throw_error
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)

            


