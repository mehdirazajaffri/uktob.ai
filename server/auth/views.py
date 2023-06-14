from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt

auth_bp = Blueprint('auth', __name__)

users = {}
bcrypt = Bcrypt()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input. Expected a JSON object with "username" and "password".'}), 400

    username = data['username']
    password = data['password']

    if username in users:
        return jsonify({'error': 'Username already exists. try another one'}), 400
    
    users[username] = bcrypt.generate_password_hash(password).decode('utf-8')
    return jsonify({'message': 'Registration successful.'}), 200


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input. Expected a JSON object with "username" and "password".'}), 400

    username = data['username']
    password = data['password']

    if username not in users or not bcrypt.check_password_hash(users[username], password):
        return jsonify({'message': 'Access denied.'}), 401

    return jsonify({'message': 'Access granted.'}), 200
