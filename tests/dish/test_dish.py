from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Restriction, Ingredient  # noqa: F401, E261, E501
import pytest # noqa: F401, E261, E501


# Req 2
def test_dish():
    lasanha_dish = Dish("lasanha", 9.99)
    strogonof_dish = Dish("strogonof", 12.99)
    dish_restrictions = {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.GLUTEN,
    }

    with pytest.raises(TypeError):
        Dish("lasanha", "invalid_price")

    with pytest.raises(ValueError):
        Dish("strogonof", 0)

    assert isinstance(lasanha_dish, Dish)
    assert lasanha_dish.name == "lasanha"
    assert lasanha_dish.__repr__() == "Dish('lasanha', R$9.99)"
    assert lasanha_dish.__eq__(lasanha_dish) is True
    assert lasanha_dish.__eq__(strogonof_dish) is False
    assert lasanha_dish.__hash__() != strogonof_dish.__hash__()
    assert lasanha_dish.__hash__() == hash("Dish('lasanha', R$9.99)")

    cheese_ingredient = Ingredient("queijo parmesão")
    ham_ingredient = Ingredient("presunto")
    lasagna_dough_ingredient = Ingredient("massa de lasanha")

    lasanha_dish.add_ingredient_dependency(cheese_ingredient, 2)
    lasanha_dish.add_ingredient_dependency(ham_ingredient, 2)
    lasanha_dish.add_ingredient_dependency(lasagna_dough_ingredient, 2)

    assert lasanha_dish.recipe == {
        cheese_ingredient: 2,
        ham_ingredient: 2,
        lasagna_dough_ingredient: 2,
    }
    assert lasanha_dish.get_ingredients() == {
        cheese_ingredient,
        ham_ingredient,
        lasagna_dough_ingredient,
    }
    assert lasanha_dish.get_restrictions() == dish_restrictions
