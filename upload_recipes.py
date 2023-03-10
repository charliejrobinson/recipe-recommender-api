from call_api import create_new_recipe, search_by_name
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

# uploading duplicates?
def upload_all_recipes(filtered_recipes, upload_duplicates=False):

    for recipe in filtered_recipes:

        if not upload_duplicates:
            recipe_name = filtered_recipes[recipe]['name']

            # checks for duplicate
            name_alreaady_exists_request = search_by_name(recipe_name)

            if name_alreaady_exists_request.status_code != 404:
                print(f'Recipe with name {recipe_name} already exists. Recipe not uploaded due to upload_duplicates={upload_duplicates}')
                continue

        new_recipe_request = create_new_recipe(filtered_recipes[recipe])
        
        # error handling for invalid upload request
        if new_recipe_request.status_code == 400:
            print(new_recipe_request.json()['message'] + ' recipe id: ' + recipe)
            print('halting upload')
            break

recipes_data = read_recipe_file('recipes.json')
filtered_recipes = filter_recipes(recipes_data)
upload_all_recipes(filtered_recipes, upload_duplicates=False)