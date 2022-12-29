from flask import Flask, request, make_response
import firebase_admin
from firebase_admin import firestore
from validation_rules import *

# Application Default credentials are automatically created
app = firebase_admin.initialize_app()
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'


@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    docs = db.collection('recipe').stream()

    recipes = {'recipes': []}

    for doc in docs:
        recipe = doc.to_dict()
        recipe['id'] = doc.id
        recipes['recipes'].append(recipe)

    return recipes


@app.route('/recipe/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):

    try:
        doc_ref = db.collection('recipe').document(recipe_id)
        doc_ref.delete()
        return make_response(
            f'Recipe {recipe_id} deleted',
            200
        )
    except:
        return make_response(
            f'Recipe not deleted, Recipe {recipe_id} not found',
            404
        )
    

@app.route('/recipe/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):

    try:
        doc_ref = db.collection('recipe').document(recipe_id)
        doc = doc_ref.get()
    except:
        return make_response(
            'Recipe not found',
            404
        )

    recipe = doc.to_dict()
    recipe['id'] = doc.id
    
    return recipe

@app.route('/recipe', methods=['PUT'])
def put_recipe():
    body = request.get_json()

    valid_request, _, errors = validate(body, rules=put_recipe_rules, return_info=True)

    if not valid_request:
        return make_response(
        'Invalid request',
        501)


    doc_ref = db.collection('recipe').document()
    doc_ref.set({
        'name': body['name'],
        'ingredients': body['ingredients'],
        'instructions': body['instructions']
    })

    return make_response(
        'Recipe added',
        200)

    

app.run(host='0.0.0.0', port=81)