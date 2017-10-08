from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/html')
def hello():
    return 'Hello World!'


@app.route('/json')
def json():
    return jsonify({'hello': 'world'})
