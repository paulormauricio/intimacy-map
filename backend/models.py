from datetime import datetime
from database import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    notes = db.Column(db.Text, default='')
    health_score = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Stakeholder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64))
    influence = db.Column(db.String(32))
    strength = db.Column(db.String(32))

    account = db.relationship('Account', backref=db.backref('stakeholders', lazy=True))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

class AccountProduct(db.Model):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    adopted = db.Column(db.Boolean, default=False)

    account = db.relationship('Account', backref=db.backref('account_products', lazy=True))
    product = db.relationship('Product')

class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    name = db.Column(db.String(128))
    stage = db.Column(db.String(64))
    score = db.Column(db.Integer, default=0)

    account = db.relationship('Account', backref=db.backref('opportunities', lazy=True))
