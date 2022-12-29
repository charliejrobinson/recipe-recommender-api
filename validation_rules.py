from validator import validate

put_recipe_rules = {
    'name': 'required|alpha', # required name, alphabetic chars only
    'ingredients': 'required|list', # required ingredients, must be list
    'instructions': 'required|string'
}