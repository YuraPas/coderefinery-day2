import pytest
from recipes import scale_amount


@pytest.mark.parametrize("amount, base, target, expected", [
    (100, 2, 3, 150),
    (100, 2, 2, 100),
    (100, 2, 1, 50),
    (200, 4, 6, 300),
    (0, 2, 4, 0),
    (0.1, 3, 7, 0.23333333333333334),
])
def test_scaling(amount, base, target, expected):
    assert scale_amount(amount, base, target) == pytest.approx(expected)


@pytest.mark.parametrize("amount, base, target", [
    (-1, 2, 3),
    (100, 0, 3),
    (100, 2, 0),
    (100, 2, -1),
])
def test_invalid_input(amount, base, target):
    with pytest.raises(ValueError):
        scale_amount(amount, base, target)