def add(left, right):
    return left + right


def subtract(left, right):
    return left - right


def test_add():
    assert add(3, 4) == 7


def test_subtract():
    assert subtract(3, 4) == -1


def test_subtract_reversed_operands():
    assert subtract(4, 3) == 1
