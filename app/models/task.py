from datetime import datetime,timezone
from .base import BaseModel
from ..extensions import db


class Task(BaseModel):
    def __init__(self, name, list_id, status, priority, description=None, delivery_time=None, completed_at=None):
        self.name = name
        self.list_id = list_id
        self.status = status
        self.priority = priority
        self.description = description
        if delivery_time:
            self.delivery_time = delivery_time
        if completed_at:
            self.completed_at = completed_at
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(120),nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('task_lists.id'), nullable=False)
    delivery_time = db.Column(db.TIMESTAMP(timezone=True),default=lambda:datetime.now(timezone.utc))
    priority = db.Column(db.Integer,nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)