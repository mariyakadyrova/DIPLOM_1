import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient_adds_item(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_removes_by_index(self):
        burger = Burger()
        ing1, ing2 = Mock(), Mock()
        burger.ingredients = [ing1, ing2]

        burger.remove_ingredient(0)

        assert burger.ingredients == [ing2]

    def test_move_ingredient_moves_item(self):
        burger = Burger()
        ing1, ing2, ing3 = Mock(), Mock(), Mock()
        burger.ingredients = [ing1, ing2, ing3]

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ing2, ing3, ing1]

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected",
        [
            (100, [], 200),                 # булка * 2
            (100, [50], 250),               # булка*2 + 50
            (200, [10, 20, 30], 460),       # 400 + 60
        ],
    )
    def test_get_price_calculates_total(self, bun_price, ingredient_prices, expected):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        burger.ingredients = []
        for p in ingredient_prices:
            ing = Mock()
            ing.get_price.return_value = p
            burger.add_ingredient(ing)

        assert burger.get_price() == expected

    def test_get_receipt_contains_expected_lines(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 50

        filling = Mock()
        filling.get_type.return_value = "FILLING"
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 100

        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        receipt = burger.get_receipt()

        # булка сверху и снизу
        assert "(==== black bun ====)" in receipt
        # тип приводится к lower()
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        # цена: 100*2 + 50 + 100 = 350
        assert "Price: 350" in receipt
