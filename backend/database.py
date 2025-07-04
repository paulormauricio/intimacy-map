from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Initialize SQLAlchemy without app, to use application factory

db = SQLAlchemy()


def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get(
        'DATABASE_URI', 'postgresql://sam:sam@db:5432/sam')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
