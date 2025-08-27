# services/statistics_service.py
from app.models import Task
from sqlalchemy import func
from datetime import datetime
from app.extensions import db

class StatisticsService:
    @staticmethod
    def count_completed_tasks():
        # Conta tasks com completed_at preenchido (concluídas)
        return Task.query.filter(Task.completed_at != None).count()

    @staticmethod
    def count_pending_tasks():
        # Conta tasks com status 'pendente' (não concluídas)
        return Task.query.filter(Task.status == "pendente").count()

    @staticmethod
    def get_task_completion_time(task_id):
        # Busca task pelo id e calcula o tempo de conclusão
        task = Task.query.get(task_id)
        if task and task.completed_at and task.created_at:
            return (task.completed_at - task.created_at).total_seconds()
        return None

    @staticmethod
    def average_completion_time():
        # Calcula o tempo médio de conclusão das tasks
        tasks = Task.query.filter(Task.completed_at != None, Task.created_at != None).all()
        if not tasks:
            return None
        total = sum([(t.completed_at - t.created_at).total_seconds() for t in tasks])
        return total / len(tasks)
