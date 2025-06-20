from flask import Blueprint, request, jsonify
from .ml.optimizer import optimize_portfolio

main = Blueprint('main', __name__)

@main.route('/api/ping')
def ping():
    return jsonify({"message": "pong"})

@main.route('/api/portfolio/optimize', methods=['POST'])
def portfolio_optimize():
    try:
        data = request.get_json()
        assets = data['assets']
        start_date = data.get('start_date', '2023-01-01')
        end_date = data.get('end_date', '2024-01-01')

        result = optimize_portfolio(assets, start_date, end_date)
        return jsonify(result)
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Server error: " + str(e)}), 500
