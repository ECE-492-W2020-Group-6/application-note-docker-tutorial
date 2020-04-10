import pytest
from pyconstrain.constrain import constrain

@pytest.mark.parametrize("x,a,b,expected", [
    (5, -5, 10, 5),
    (5, 7, 10, 7),
    (5, -11, 2, 2),
])
def test_constrain(x,a,b,expected):
    assert constrain(x,a,b) == expected
