# controllers/task_controller.py
from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService
from flask_jwt_extended import jwt_required


task_bp = Blueprint('tasks', __name__, url_prefix=__name__)

@task_bp.route('/', methods=['POST'])
@jwt_required()
def create_task():
    data = request.json
    required_fields = ['name', 'list_id', 'priority']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    task = TaskService.create_task(
        name=data['name'],
        list_id=data['list_id'],
        priority=data['priority'],
        description=data.get('description', "")
    )
    return jsonify({
        "id": task.id,
        "name": task.name,
        "status": task.status,
        "priority": task.priority,
        "list_id": task.list_id,
        "created_at": task.created_at.isoformat() if task.created_at else None,
        "updated_at": task.updated_at.isoformat() if task.updated_at else None,
        "delivery_time": task.delivery_time.isoformat() if task.delivery_time else None
    }), 201

@task_bp.route('/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    task = TaskService.get_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({
        "id": task.id,
        "name": task.name,
        "status": task.status,
        "priority": task.priority,
        "list_id": task.list_id,
        "created_at": task.created_at.isoformat() if task.created_at else None,
        "updated_at": task.updated_at.isoformat() if task.updated_at else None,
        "delivery_time": task.delivery_time.isoformat() if task.delivery_time else None
    })

@task_bp.route('/list/<int:list_id>', methods=['GET'])
def get_tasks_by_list(list_id):
    tasks = TaskService.get_tasks_by_list(list_id)
    return jsonify([
        {
            "id": t.id,
            "name": t.name,
            "status": t.status,
            "priority": t.priority,
            "list_id": t.list_id,
            "created_at": t.created_at.isoformat() if t.created_at else None,
            "updated_at": t.updated_at.isoformat() if t.updated_at else None,
            "delivery_time": t.delivery_time.isoformat() if t.delivery_time else None
        }
        for t in tasks
    ])

@task_bp.route('/<int:task_id>', methods=['PATCH'])
@jwt_required()
def update_task(task_id):
    data = request.json
    task = TaskService.update_task(task_id, **data)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({
        "id": task.id,
        "name": task.name,
        "status": task.status,
        "priority": task.priority,
        "list_id": task.list_id
    })

@task_bp.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    success = TaskService.delete_task(task_id)
    if not success:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted"})
