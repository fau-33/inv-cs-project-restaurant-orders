from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    frango_ingredient = Ingredient("frango")
    salmao_ingredient = Ingredient("salmão")
    frango_restrictons = {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT
    }

    assert isinstance(frango_ingredient, Ingredient)
    assert frango_ingredient.__hash__() != salmao_ingredient.__hash__()
    assert frango_ingredient.__hash__() == hash("frango")
    assert frango_ingredient.__eq__(frango_ingredient) is True
    assert frango_ingredient.__eq__(salmao_ingredient) is False
    assert frango_ingredient.__repr__() == "Ingredient('frango')"
    assert frango_ingredient.name == "frango"
    assert frango_ingredient.restrictions == frango_restrictons
