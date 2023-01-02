from call_api import create_new_recipe
import json

############################
# TO DO - Clear all recipes
############################


# Read and return a recipes file (json)
def read_recipe_file(filename):
    with open(filename, 'r') as recipes_json_file:
        recipes_data = json.load(recipes_json_file)
        return recipes_data

# extract fields we want (currently name, instructions, ingredients)
def filter_recipes(recipes):

    # new json to store filtered recipes -> can maybe do this more elegantly
    # {
    # id: {
    #   name: String
    #   ingredients: List
    #   instructions: String 
    #   }
    # }
    filtered_recipes = {}

    for recipe in recipes:

        recipe_obj = recipes[recipe]

        id = recipe_obj['id']
        name = recipe_obj['name']
        ingredients = recipe_obj['ingredients']
        instructions = recipe_obj['instructions']
        
        # contingent on provided recipes json having unique ids -> else will overwrite existing ids -> could do check
        filtered_recipes[id] = {}
        filtered_recipes[id]['name'] = name
        filtered_recipes[id]['ingredients'] = ingredients
        filtered_recipes[id]['instructions'] = instructions

    
    return filtered_recipes

def upload_all_recipes(filtered_recipes):

    for recipe in filtered_recipes:
        create_new_recipe(filtered_recipes[recipe])
        break

recipes_data = read_recipe_file('recipes.json')
filtered_recipes = filter_recipes(recipes_data)
upload_all_recipes(filtered_recipes)