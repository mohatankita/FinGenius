from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/api/ping')
def ping():
    return jsonify({"message": "pong"})