from flask_httpauth import HTTPBasicAuth
from ..models.auth import User
from .errors import unauthorized
from . import api

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(name, password):
    if name == '':
        return False
    user = User(name, '', '')
    user.password = '12345'
    if not user:
        return False
    return user.verify_password(password)

@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')

@api.before_request
@auth.login_required
def before_request():
    pass