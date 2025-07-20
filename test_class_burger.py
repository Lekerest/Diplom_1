import pytest
from unittest.mock import Mock
from burger import Burger


# -------------------- ФИКСТУРЫ --------------------

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


# -------------------- ТЕСТЫ --------------------

class TestBurger:

    def test_init_(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_set_buns(self, create_bun):
        burger = Burger()
        burger.set_buns(create_bun)
        assert burger.bun is create_bun

    def test_add_ingredient(self, ingredient_1):
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        assert burger.ingredients == [ingredient_1]

    def test_remove_ingredient(self, ingredient_1):
        burger = Burger()
        burger.ingredients = [ingredient_1]
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, ingredient_1, ingredient_2):
        burger = Burger()
        burger.ingredients = [ingredient_1, ingredient_2]
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    @pytest.mark.parametrize(
        "bun_price, ing_prices, expected_total",
        [
            (1.0, [1.0], 3.0),
            (1.5, [0.5, 0.5], 4.0),
            (3.0, [], 6.0),
        ]
    )
    def test_get_price(self, bun_price, ing_prices, expected_total):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.bun = bun

        ingredients = []
        for price in ing_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            ingredients.append(ingredient)
        burger.ingredients = ingredients

        assert burger.get_price() == expected_total

    def test_get_receipt_with_mock(self, create_bun, ingredient_1, ingredient_2):
        burger = Burger()
        burger.bun = create_bun
        burger.ingredients = [ingredient_1, ingredient_2]

        expected_receipt = (
            f"(==== {create_bun.get_name()} ====)\n"
            f"= {ingredient_1.get_type().lower()} {ingredient_1.get_name()} =\n"
            f"= {ingredient_2.get_type().lower()} {ingredient_2.get_name()} =\n"
            f"(==== {create_bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )

        assert burger.get_receipt() == expected_receipt
