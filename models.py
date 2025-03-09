from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class Member(db.Model):
    __tablename__ = 'members'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    booking_count = db.Column(db.Integer, default=0)
    date_joined = db.Column(db.DateTime, nullable=False)
    
    # Relationship with bookings
    bookings = db.relationship('Booking', backref='member', lazy=True)
    
    def __repr__(self):
        return f"<Member {self.name} {self.surname}>"

class Inventory(db.Model):
    __tablename__ = 'inventory'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    remaining_count = db.Column(db.Integer, default=0)
    expiration_date = db.Column(db.Date, nullable=False)
    
    # Relationship with bookings
    bookings = db.relationship('Booking', backref='item', lazy=True)
    
    def __repr__(self):
        return f"<Inventory {self.title}>"

class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    booking_reference = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f"<Booking {self.booking_reference}>"