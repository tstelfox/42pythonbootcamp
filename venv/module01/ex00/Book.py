class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list
    # def get_recipe_by_name(self, name):
    def add_recipe(self, recipe):

