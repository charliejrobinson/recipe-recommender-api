import requests
from pprint import pprint

host_add = 'http://192.168.1.199:81'

# Send PUT request to create new recipe
def create_new_recipe(data):
    r = requests.put(f'{host_add}/recipes', json=data)
    print(r.json())

# Send PUT request to update recipe
def update_recipe(id, data):
    r = requests.put(f'{host_add}/recipe/{id}', json=data)
    print(r.json())

# Send GET request to get a recipe from id
def get_recipe(id):
    r = requests.get(f'{host_add}/recipe/{id}')
    print(r.json())

# Send DELETE request to delete a recipe from id
def delete_recipe(id):
    r = requests.delete(f'{host_add}/recipe/{id}')
    print(r.json())

# Send GET request to get all recipes
def get_all_recipes():
    r = requests.get(f'{host_add}/recipes')
    print(r.json())

# validate data
# clean up code
# add query route
# add comments & documentation
# validate request : if object doesn't exist, return 404
# vue / IFTT

data = {
    'name': 3,
    'ingredients': ['radish','honey'],
    'instructions': 'Put in oven'
}

get_all_recipes()