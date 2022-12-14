import pytest

from project1 import Pizza


def test_1():
    some_pizza = Pizza('Some_name', 'L', ['tomato sauce', 'mozzarella', 'tomatoes'])
    assert some_pizza.dict() == {'Some_name': 'tomato sauce,mozzarella,tomatoes'}


def test_2():
    with pytest.raises(ValueError):
        some_pizza = Pizza('Some_name', 'M', ['tomato sauce', 'mozzarella', 'tomatoes'])


def test_3():
    some_pizza = Pizza('Some_name', 'L', ['tomato sauce', 'mozzarella', 'tomatoes', 'olives'])
    assert some_pizza.dict() == {'Some_name': 'tomato sauce,mozzarella,tomatoes,olives'}