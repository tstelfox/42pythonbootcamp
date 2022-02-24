cookbook = {
    'sandwich': {'ingredients': ["ham", "bread", "cheese", "tomatoes"], 'meal': "lunch", 'prep_time': 10},
    'cake': {'ingredients': ["flour", "sugar", "eggs"], 'meal': "dessert", 'prep_time': 60},
    'salad': {'ingredients': ["avocado", "rucola", "toamtoes", "spinach" ], 'meal': "lunch", 'prep_time': 15}
}

def display_recipe(name):
    print(cookbook[name])

def delete_recipe(name):
    del cookbook[name]

def add_recipe(name, ingredients, type, prep_time):
    cookbook[name] = {'ingredients': ingredients, 'type': type, 'prep_time': prep_time}

def print_recipes():
    for dish, recipe in cookbook.items():
        print("Recipe for:", dish.ljust(15, "-"))
#
# display_recipe('cake')
# delete_recipe('cake')
# add_recipe("Mumyer puddin", ["mumyer", "a", 90], "breakfastlunchndinner", 69)
# # print(cookbook)
# print_recipes()

if __name__ == "__main__":
    # functions = {
    #     1:
    # }
    print("Welcome to Turlough's recipe book, what would you like to do?")
    # print("A) Add a recipe\nB) Delete a recipe\nC) Print a recipe\nD) Print the cookbook\nE) Exit")
    while 1:
        action = input("\n1) Add a recipe\n2) Delete a recipe\n3) Print a recipe\n4) Print the cookbook\n5) Exit\n>>> ")
        if action == "1":
            name = input("Name of recipe: ")
            ingredients = input("Ingredients separated by a space: ").split()
            type = input("Type: ")
            prep_time = input("How long this shit take? ")
            add_recipe(name, ingredients, type, prep_time)
        # if action == 1:
        elif action == "2":
            delete_recipe(input("Which recipe would you like to remove?\n>>> "))
        elif action == "3":
            display_recipe(input("Which recipe would you like to view?\n>>> "))
            # print("\n")
        elif action == "4":
            print("Printing the whole cookbook:")
            print_recipes()
            # print("\n")
        elif action == "5":
            print("Bona ciao")
            exit()
        else:
            print("WHAT ARE YOU DOING? THIS IS A COOKBOOK SON")
# for dish, recipe in cookbook.items():
#     print("\nDish name: ", dish)
#
#     for section in recipe:
#         print(section + ":", recipe[section])


