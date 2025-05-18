# app/routes.py
from flask import Blueprint, request, jsonify
from .models import Notification
from . import db

api = Blueprint('api', __name__)

@api.route('/notifications', methods=['POST'])
def send_notification():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400

    data = request.get_json()
    print(f"Incoming JSON: {data}")

    required_fields = ['user_id', 'type', 'content']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    notif = Notification(
        user_id=data['user_id'],
        type=data['type'],
        content=data['content']
    )
    db.session.add(notif)
    db.session.commit()

    print(f"Simulated send: {notif.type.upper()} to user {notif.user_id}: {notif.content}")

    return jsonify({'message': 'Notification sent', 'id': notif.id}), 201

@api.route('/users/<user_id>/notifications', methods=['GET'])
def get_notifications(user_id):
    notifs = Notification.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': n.id,
        'type': n.type,
        'content': n.content,
        'status': n.status,
        'created_at': n.created_at.isoformat()
    } for n in notifs])
