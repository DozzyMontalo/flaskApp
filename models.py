# models.py
from extention import db

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    guest_name = db.Column(db.String(100), nullable=False)

    hotel = db.relationship('Hotel', backref='bookings')

    def __repr__(self):
        return f"Booking('{self.check_in_date}', '{self.check_out_date}', '{self.guest_name}')"
    
    
