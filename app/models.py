# app/models.py
from . import db
from datetime import datetime

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(20), nullable=False)  # email, sms, in-app
    content = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), default="sent")  # always 'sent' here
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
