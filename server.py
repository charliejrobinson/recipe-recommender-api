from flask import Flask, request
import firebase_admin
from firebase_admin import firestore

# Ingredients I have in the fridge
# What can I make?

# Application Default credentials are automatically created.
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
    doc_ref = db.collection('recipe').document(recipe_id)
    doc_ref.delete()
    
    return {'message': 'Recipe deleted'}

@app.route('/recipe/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    doc_ref = db.collection('recipe').document(recipe_id)
    doc = doc_ref.get()
    
    if doc.empty:
        return {'message': 'recipe not found'}

    recipe = doc.to_dict()
    recipe['id'] = doc.id
    
    return recipe

@app.route('/recipe', methods=['PUT'])
def put_recipe():
    body = request.get_json()
    print(body)

    doc_ref = db.collection('recipe').document()
    doc_ref.set({
        'name': body['name'],
        'ingredients': body['ingredients'],
        'instructions': body['instructions']
    })

    return body

app.run(host='0.0.0.0', port=81)