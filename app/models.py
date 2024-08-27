from .extensions import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    data_publish = db.Column(db.DateTime, default=datetime.utcnow)
    rate = db.Column
    image = db.Column(db.String(255), nullable=True)