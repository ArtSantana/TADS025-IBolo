from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    response = jsonify(response_value_1=1,response_value_2="value")
    return response, 200

@app.errorhandler(405)
def page_not_found(error):
    return 'Method not allowed', 404