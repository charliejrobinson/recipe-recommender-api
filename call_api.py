import requests
from pprint import pprint

host_add = 'http://192.168.1.199:81'

# Send PUT request to create new recipe
def create_new_recipe(data):
    r = requests.put(f'{host_add}/recipes', json=data)
    return r.json()

# Send PUT request to update recipe
def update_recipe(id, data):
    r = requests.put(f'{host_add}/recipe/{id}', json=data)
    return r.json()

# Send GET request to get a recipe from id
def get_recipe(id):
    r = requests.get(f'{host_add}/recipe/{id}')
    return r.json()

# Send DELETE request to delete a recipe from id
def delete_recipe(id):
    r = requests.delete(f'{host_add}/recipe/{id}')
    return r.json()

# Send GET request to get all recipes
def get_all_recipes():
    r = requests.get(f'{host_add}/recipes')
    return r.json()

# Send GET request to search for recipe by name
def search_by_name(recipe_name):
    r = requests.get(f'{host_add}/recipes/search?name={recipe_name}')
    return r.json()


# add comments & documentation
# vue / IFTT -> hosting
# add limit for query, pagination (flask?)