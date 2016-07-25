'''
Decorator and supporting functions to authenticate API requests.

Started with the Authorization section of this page.

http://blog.luisrei.com/articles/flaskrest.html
'''

from flask import jsonify
from flask import request

import bcrypt

from functools import wraps


def check_auth(username, password):
    ''' In a real world application this would be checked against a database '''
    password_hash = "$2b$12$qUaVSupX6R1UBXKoqt/0dOd8CmLtM5Q4rarpCX3C4O3jRm56pIOYy"
    return username == 'bob' and bcrypt.hashpw(password, password_hash) == password_hash


def authenticate():
    message = {'status': 401, 'message': 'Authentication required'}
    response = jsonify(message)
    response.status_code = 401
    response.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return response


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
