from app import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    unit = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Integer, default=3)