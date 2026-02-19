from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_available_buns_returns_list_of_buns(self):
        db = Database()
        buns = db.available_buns()

        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(isinstance(b, Bun) for b in buns)

    def test_available_ingredients_returns_list_of_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(isinstance(i, Ingredient) for i in ingredients)
