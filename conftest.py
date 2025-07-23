import pytest
from unittest.mock import Mock

@pytest.fixture
def create_bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = "Обычная"
    bun_mock.get_price.return_value = 2.55
    return bun_mock


@pytest.fixture
def ingredient_1():
    ingredient_mock = Mock()
    ingredient_mock.get_type.return_value = "Соус"
    ingredient_mock.get_name.return_value = "Кетчуп"
    ingredient_mock.get_price.return_value = 0.99
    return ingredient_mock


@pytest.fixture
def ingredient_2():
    ingredient_mock = Mock()
    ingredient_mock.get_type.return_value = "Соус"
    ingredient_mock.get_name.return_value = "Майонез"
    ingredient_mock.get_price.return_value = 1.99
    return ingredient_mock