"""
This module collects all the Data Transfer Objects for the API
"""
from flask_restplus import Namespace, fields


class UserDTO(object):
    """User Data Transfer Object"""
    api = Namespace('auth', description='user authentication and signup resources')
    n_user = api.model('new user request', {
        'first_name': fields.String(required=True, description="user's first name"),
        'last_name': fields.String(required=True, description="user's last name"),
        'username': fields.String(required=True, description="user's username"),
        'email': fields.String(required=True, description="user's email address"),
        'password': fields.String(required=True, description="user's password")
    })
    n_user_resp = api.model('response to signup', {
        'message': fields.String(required=True, description="success or fail message"),
        'AuthToken': fields.String(required=True, description="authentication token"),
        'username': fields.String(required=True, description="user's username"),
        'user_id': fields.String(required=True, description="user's id")
    })
    user_resp = api.model('response to login', {
        'message': fields.String(required=True, description="success or fail message"),
        'AuthToken': fields.String(required=True, description="authentication token"),
        'name': fields.String(required=True, description="user's username"),
        'date_created': fields.String(required=True, description="user's id")
    })
    user = api.model('login request', {
        'username': fields.String(required=True, description="user's username"),
        'password': fields.String(required=True, description="user's password")
    })
    user_logout = api.model('logout request', {
        'message': fields.String(required=True, description="success message")
    })
