from flask import Blueprint, request, jsonify
from models.models import Recipe, db

recipe_blueprint = Blueprint('recipe', __name__)

@recipe_blueprint.route('/recipes', methods=['GET'])
def get_all_recipes():
    recipes = Recipe.query.all()
    output = []
    for recipe in recipes:
        recipe_data = {}
        recipe_data['id'] = recipe.id
        recipe_data['name'] = recipe.name
        recipe_data['ingredients'] = recipe.ingredients
        recipe_data['instructions'] = recipe.instructions
        recipe_data['cooking_time'] = recipe.cooking_time
        recipe_data['dietary_restriction'] = recipe.dietary_restriction
        output.append(recipe_data)
    return jsonify({'recipes': output})

@recipe_blueprint.route('/recipes/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe is None:
        return jsonify({'message': 'Recipe not found'}), 404
    recipe_data = {}
    recipe_data['id'] = recipe.id
    recipe_data['name'] = recipe.name
    recipe_data['ingredients'] = recipe.ingredients
    recipe_data['instructions'] = recipe.instructions
    recipe_data['cooking_time'] = recipe.cooking_time
    recipe_data['dietary_restriction'] = recipe.dietary_restriction
    return jsonify({'recipe': recipe_data})

@recipe_blueprint.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        name=data['name'],
        ingredients=data.get('ingredients', []),
        instructions=data.get('instructions', ''),
        cooking_time=data.get('cooking_time', 0),
        dietary_restriction=data.get('dietary_restriction', '')
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe created successfully'}), 201

@recipe_blueprint.route('/recipes/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe is None:
        return jsonify({'message': 'Recipe not found'}), 404
    data = request.get_json()
    recipe.name = data.get('name', recipe.name)
    recipe.ingredients = data.get('ingredients', recipe.ingredients)
    recipe.instructions = data.get('instructions', recipe.instructions)
    recipe.cooking_time = data.get('cooking_time', recipe.cooking_time)
    recipe.dietary_restriction = data.get('dietary_restriction', recipe.dietary_restriction)
    db.session.commit()
    return jsonify({'message': 'Recipe updated successfully'})

@recipe_blueprint.route('/recipes/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe is None:
        return jsonify({'message': 'Recipe not found'}), 404
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe deleted successfully'})