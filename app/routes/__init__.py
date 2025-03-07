from flask import Blueprint

register_routes = Blueprint('routes', __name__)

from .routes import routes

__all__ = ['routes']