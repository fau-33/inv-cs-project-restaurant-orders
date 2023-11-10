import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        all_dishes = {}
        with open(source_path, encoding='UTF-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row['dish']
                price = float(row['price'])
                ingredient = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                if dish_name not in all_dishes:
                    all_dishes[dish_name] = Dish(dish_name, price)

                all_dishes[dish_name].add_ingredient_dependency(
                    Ingredient(ingredient), recipe_amount
                )

        self.dishes = set(all_dishes.values())
