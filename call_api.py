import requests
from pprint import pprint

host_add = http://192.168.1.199:81

data = {
    'name': 'recipe test 2',
    'ingredients': ['a','b'],
    'instructions': ['c','d']
}

# Send PUT request to create new recipe
def put_new_recipe(data):
    p = requests.put(f'{host_add}/recipe', json=data)

# Send PUT request to update recipe
def put_update_recipe(data):
    p = requests.put(f'{host_add}/recipe', json=data)

# Send GET request to get a recipe from id
def get_recipe(id):
    pass

# Send GET request to get all recipes (all data)
def get_all_recipes_data():
    g = requests.get(f'{host_add}/recipes')

# Send GET request to get all recipes (all ids)
def get_all_recipes_id():
    g = requests.get(f'{host_add}/recipes')

# Send DELETE request to delete a recipe from id
def delete_recipe(id):
    d = requests.delete(f'http://192.168.1.199:81/recipe/{id}')

# Send DELETE request to delete all recipes
def delete_all_recipes():
    pass

# validate data
# clean up code
# add query route
# add comments & documentation
# validate request : if object doesn't exist, return 404
# vue