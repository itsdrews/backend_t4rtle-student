# controllers/statistics_controller.py
from flask import Blueprint, jsonify, request
from app.services.statistics_service import StatisticsService
from flask_jwt_extended import jwt_required

statistics_bp = Blueprint('statistics', __name__)

@statistics_bp.route('/tasks/completed', methods=['GET'])
@jwt_required()
def count_completed_tasks():
    count = StatisticsService.count_completed_tasks()
    return jsonify({"completed_tasks": count})

@statistics_bp.route('/tasks/pending', methods=['GET'])
@jwt_required()
def count_pending_tasks():
    count = StatisticsService.count_pending_tasks()
    return jsonify({"pending_tasks": count})

@statistics_bp.route('/tasks/<int:task_id>/completion_time', methods=['GET'])
@jwt_required()
def get_task_completion_time(task_id):
    seconds = StatisticsService.get_task_completion_time(task_id)
    return jsonify({"completion_time_seconds": seconds})

@statistics_bp.route('/tasks/average_completion_time', methods=['GET'])
@jwt_required()
def average_completion_time():
    avg = StatisticsService.average_completion_time()
    return jsonify({"average_completion_time_seconds": avg})
