from flask_sqlalchemy import SQLAlchemy
from .models import Account, Goal
db = SQLAlchemy()

__all__ = ['db', 'Account', 'Goal']