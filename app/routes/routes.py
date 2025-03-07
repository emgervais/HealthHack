from flask import Blueprint, request, jsonify, render_template
from app.models import db, Account, Goal
import random

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/api/goals', methods=['POST'])
def update_score():
    data = request.get_json()
    score_value = data.get('score')
    if score_value is None:
        return jsonify({'error': 'Score value is required'}), 400

    new_score = Account(value=score_value)
    db.session.add(new_score)
    db.session.commit()

    return jsonify({'message': 'Score updated successfully'}), 201

@routes.route('/api/goals', methods=['GET'])
def new_goals():
    goals = Goal.query.all()
    random_number = random.randint(0, len(goals) - 1)
    goal = goals[random_number]
    
    return jsonify({'id': goal.id, 'title': goal.title, 'description': goal.description, 'unit': goal.unit}), 200