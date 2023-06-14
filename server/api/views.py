# api.py
from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__)

@api_bp.route('/sum', methods=['POST'])
def sum_numbers():
    try:
        data = request.get_json()
        if not data or 'numbers' not in data or not isinstance(data['numbers'], list):
            return jsonify({'error': 'Invalid input. Expected a JSON object with a list of numbers.'}), 400
        
        numbers = data['numbers']
        try:
            result = sum(numbers)
            return jsonify({'sum': result}), 200
        except TypeError:
            return jsonify({'error': 'Invalid input. Numbers should be integers or floats.'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred.', 'message': str(e)}), 500

@api_bp.route('/concatenate', methods=['POST'])
def concatenate_strings():
    data = request.get_json()
    if not data or 'strings' not in data or not isinstance(data['strings'], list):
        return jsonify({'error': 'Invalid input. Expected a JSON object with a list of strings.'}), 400

    strings = data['strings']
    if not all(isinstance(s, str) for s in strings):
        return jsonify({'error': 'Invalid input. All values in the list should be strings.'}), 400

    result = ''.join(strings)
    return jsonify({'concatenated': result}), 200
