import pytest
from calculator import add, substract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_substract():
    assert substract(5, 3) == 2
    assert substract(0, 5) == -5
    assert substract(10, 10) == 0


def test_add_type_error():
    with pytest.raises(TypeError):
        add("2", 3)