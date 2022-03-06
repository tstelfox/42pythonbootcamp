class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        if cooking_lvl > 5 or cooking_lvl < 1:
            print("Cooking level of ", cooking_lvl, "is incorrect")
            exit()
        if (cooking_time < 0):
            print("No negative cooking time")
            exit()
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    def __str__(self):
        print("The recipe for" + name + "")


Mio = Recipe("Carbonara", 2, 25, ["uova", "guanciale", "pecorino romano"], "Bona in culo", "primo")

print(Mio.ingredients)