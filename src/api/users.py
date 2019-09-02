from flask import jsonify
from . import api
from ..models.auth import User

@api.route('/users/')
def get_users():
    users = [
        User("Raphael", 'jf', 'developer'),
        User("Castilho", 'rj', 'architect'),
        User("Costa", 'sp', 'tester')
    ]
    users_json = {'users': [user.to_json() for user in users]}
    return jsonify(users_json)