from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    asset_tag = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    status = db.Column(db.String(32), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
