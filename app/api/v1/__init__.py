"""
This module sets up the users resource
Authored by: Lenny Kamande
"""
from flask_restplus import Api
from flask import Blueprint
from werkzeug.exceptions import NotFound

version1 = Blueprint('version1', __name__, url_prefix="/api/v1")

from .endpoints.auth_endpoints import api as auth_ns


api = Api(version1,
          title='ALU User API',
          version='1.0',
          description="An amateur's simulation of the a login system")

api.add_namespace(auth_ns, path="/auth")
