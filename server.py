from flask import Flask, request, make_response
import firebase_admin
from firebase_admin import firestore

from validator import validate
from validation_rules import *

# Create Firebase app
app = firebase_admin.initialize_app()
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

# Return all recipes from database
@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    docs = db.collection('recipe').stream()

    recipes = {'recipes': []}

    for doc in docs:
        recipe = doc.to_dict()
        recipe['id'] = doc.id
        recipes['recipes'].append(recipe)

    return make_response(
        {
            'recipes': recipes
        },
        200
    )

# Delete a recipe from id
@app.route('/recipe/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):

    doc_ref = db.collection('recipe').document(recipe_id)
    doc_ref.delete()
    
    return make_response(
            {
                'message': f'Recipe {recipe_id} deleted'
            },
            200
        )
    
# Return recipe info from id
@app.route('/recipe/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):

    try:
        doc_ref = db.collection('recipe').document(recipe_id)
        doc = doc_ref.get()
    except:
        return make_response(
            {
                'message': 'Recipe not found'
            },
            404
        )

    recipe = doc.to_dict()
    recipe['id'] = doc.id
    
    return make_response(
        {
            'recipe': recipe
        },
        200
    )

# Update recipe from id
@app.route('/recipe/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):

    try:
        doc_ref = db.collection('recipe').document(recipe_id)
    except:
        return make_response(
            {
                'message': f'Recipe {recipe_id} not found'
            },
            404
        )

    body = request.get_json()

    valid_request, _, errors = validate(body, rules=put_recipe_rules, return_info=True)

    if not valid_request:
        return make_response(
        {
            'message': 'Invalid data format',
            'errors': errors
        },
        400)

    doc_ref.set({
        'name': body['name'],
        'ingredients': body['ingredients'],
        'instructions': body['instructions']
    })

    return make_response(
        {
            'message': 'Recipe updated'
        },
        200
    )

# Create new recipe
@app.route('/recipes', methods=['PUT'])
def create_recipe():
    body = request.get_json()

    valid_request, _, errors = validate(body, rules=put_recipe_rules, return_info=True)

    if not valid_request:
        return make_response(
        {
            'message': 'Invalid data format',
            'errors': errors
        },
        400)

    doc_ref = db.collection('recipe').document()
    doc_ref.set({
        'name': body['name'],
        'ingredients': body['ingredients'],
        'instructions': body['instructions']
    })

    return make_response(
        {
            'message': f'Recipe added, id: {doc_ref}'
        },
        200)

@app.route('/recipes/search', methods=['GET'])
def search():
    name = request.args.get('name')

    query = db.collection('recipe').where('name', '==', name).stream()

    recipes = []

    for doc in query:

        recipe = doc.to_dict()
        recipe['id'] = doc.id

        recipes.append(recipe)

    if not recipes:
        return make_response(
            {
                'message': 'No recipes found'
            },
            404
        )

    return make_response(
        {
            'recipes': recipes
        },
        200
    )

app.run(host='0.0.0.0', port=81)