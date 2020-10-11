import os
import datetime
from flask import Flask, request, jsonify


UPLOAD_FOLDER = './received'
ALLOWED_EXTENSIONS = ['png']


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def hello():
    return jsonify({'msg': 'hello!'})


@app.route('/smile', methods=['POST'])
def log():
    if 'img' not in request.files:
        return jsonify({'msg': 'no file received'})
    file = request.files['img']
    if file and allowed_file(file.filename):
        filename = str(datetime.datetime.now()) + '.png'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'msg': 'file received'})


app.run(host='0.0.0.0', port=5000, debug=True)
