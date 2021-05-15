from flask import Flask, request, jsonify
from domain.ingredients.handler import HandleIngredient
from api.utils.response_generic import ResponseGeneric
from domain.config.database import database

app = Flask(__name__)

@app.route('/ingredients', methods=['GET', 'POST'])
def handler_ingredients():
    h = HandleIngredient(request)
    response = h.exec_get_post()
    return app.response_class(response=response.get_body_json(),
                                          status=response.status, 
                                          mimetype='application/json')

@app.route('/ingredients/<ingredient_id>', methods=['DELETE', 'PUT'])
def delete_ingredient(ingredient_id):
    id = ingredient_id
    h = HandleIngredient(request)
    response = h.exec_delete_put(id)

    return app.response_class(response=response.get_body_json(),
                                          status=response.status,
                                          mimetype='application/json')

@app.route('/recipes', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def handler_recipes():
    h = HandleIngredient(request)
    response = h.exec()
    return app.response_class(response=response.get_body_json(),
                                          status=response.status, 
                                          mimetype='application/json')

@app.route('/cakes', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def handler_cakes():
    h = HandleIngredient(request)
    response = h.exec()
    return app.response_class(response=response.get_body_json(),
                                          status=response.status, 
                                          mimetype='application/json')

@app.errorhandler(405)
def invalid_method(error):
    response_generic = ResponseGeneric()
    response_generic.status = 405
    response_generic.data.message = 'Method not allowed'
    return app.response_class(response=response_generic.get_body_json(),
                              status=response_generic.status,
                              mimetype='application/json')

@app.errorhandler(404)
def invalid_method(error):
    response_generic = ResponseGeneric()
    response_generic.status = 404
    response_generic.data.message = 'Not found'
    return app.response_class(response=response_generic.get_body_json(),
                              status=response_generic.status,
                              mimetype='application/json')