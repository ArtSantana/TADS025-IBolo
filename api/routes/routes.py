from flask import Flask, request
from domain.ingredients.handler import HandleIngredient
from api.utils.response_generic import ResponseGeneric

app = Flask(__name__)

@app.route('/ingredients', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def handler_ingredients():
    h = HandleIngredient(request)
    h.exec()
    response = h.exec()
    response_handled = app.response_class(response=response.get_body_json(),
                                          status=response.status, 
                                          mimetype='application/json')
    return response_handled

@app.route('/recipes', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def handler_recipes():
    h = HandleIngredient(request)
    h.exec()
    response = h.exec()
    response_handled = app.response_class(response=response.get_body_json(),
                                          status=response.status, 
                                          mimetype='application/json')
    return response_handled

@app.route('/cakes', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def handler_cakes():
    h = HandleIngredient(request)
    h.exec()
    response = h.exec()
    response_handled = app.response_class(response=response.get_body_json(),
                                          status=response.status, 
                                          mimetype='application/json')
    return response_handled

@app.errorhandler(405)
def invalid_method(error):
    response_generic = ResponseGeneric('Method not allowed', 405)
    return app.response_class(response=response_generic.get_body_json(),
                              status=response_generic.status,
                              mimetype='application/json')