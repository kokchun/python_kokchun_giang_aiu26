from vector import Vector
from pytest import raises

def test_valid_init():
    v = Vector(1,2,3)
    assert v.numbers == (1,2,3)

def test_invalid_init():
    with raises(TypeError):
        Vector(1,2,"3")

def test_invalid_empty_vector():
    with raises(ValueError):
        Vector()