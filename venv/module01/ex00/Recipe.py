class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        if cooking_lvl > 5 or cooking_lvl < 1:
            print("Cooking level of ", cooking_lvl, "is incorrect")
            exit()
        if cooking_time < 0:
            print("No negative cooking time")
            exit()
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = "The recipe for " + self.name + "\nDifficulty " + ("* " * self.cooking_lvl)
        txt += "\nRequires " + str(self.cooking_time) + " mins"
        txt += "\nIngredients: " + ', '.join(map(str, self.ingredients))
        txt += "\n\"" + self.description + "\""
        txt += "\nPortata: " + self.recipe_type
        return txt


Mio = Recipe("Carbonara", 2, 25, ["uova", "guanciale", "pecorino romano"], "Gustoso e semplice piatto tipico Romano", "primo")

print(Mio)