from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient

class TestBurger:

    def test_init_(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Обычная", 2.55)
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient("Соус", "Кетчуп", 0.99)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient("Соус", "Кетчуп", 0.99)
        burger.ingredients = [ingredient]
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient("Соус", "Кетчуп", 0.99)
        ingredient_2 = Ingredient("Соус", "Майонез", 1.99)
        burger.ingredients = [ingredient_1, ingredient_2]
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self):
        burger = Burger()
        bun = Bun("Обычная", 2.55)
        ingredient_1 = Ingredient("Соус", "Кетчуп", 0.99)
        ingredient_2 = Ingredient("Соус", "Майонез", 1.99)
        burger.bun = bun
        burger.ingredients = [ingredient_1, ingredient_2]
        expected_price = bun.get_price() * 2 + ingredient_1.get_price() + ingredient_2.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_with_mock(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "Обычная"
        mock_bun.get_price.return_value = 2.55

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = "Соус"
        mock_ingredient_1.get_name.return_value = "Кетчуп"
        mock_ingredient_1.get_price.return_value = 0.99

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = "Соус"
        mock_ingredient_2.get_name.return_value = "Майонез"
        mock_ingredient_2.get_price.return_value = 1.99

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]

        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_ingredient_1.get_type().lower()} {mock_ingredient_1.get_name()} =\n"
            f"= {mock_ingredient_2.get_type().lower()} {mock_ingredient_2.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )

        assert burger.get_receipt() == expected_receipt
