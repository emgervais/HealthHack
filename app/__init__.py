from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    
    db.init_app(app)

    from app.routes.routes import routes
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()
    
    return app