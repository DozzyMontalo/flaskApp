# routes.py
from flask import jsonify, request
from app import app, db
from models import Hotel, Booking 


@app.route('/admin/hotels', methods=['POST'])
def create_hotel():
  try:
    data = request.json
    name = data.get('name')
    location = data.get('location')
    description = data.get('description')

    hotel = Hotel(name=name, location=location, description=description)
    db.session.add(hotel)
    db.session.commit()

    return jsonify({'message': 'Hotel created successfully'}), 201
  except Exception as e:
    # Log the error for debugging
    app.logger.error(f"Error creating hotel: {e}")
    return jsonify({'message': 'An error occurred while creating the hotel'}), 500


@app.route('/admin/hotels', methods=['GET'])
def get_all_hotels():
    hotels = Hotel.query.all()
    return jsonify([{'id': hotel.id, 'name': hotel.name, 'location': hotel.location, 'description': hotel.description} for hotel in hotels])


@app.route('/hotels', methods=['GET'])
def get_hotels():
    hotels = Hotel.query.all()
    return jsonify([{'id': hotel.id, 'name': hotel.name, 'location': hotel.location, 'description': hotel.description} for hotel in hotels])

@app.route('/bookings', methods=['POST'])
def create_booking():
    data = request.json
    hotel_id = data.get('hotel_id')
    check_in_date = data.get('check_in_date')
    check_out_date = data.get('check_out_date')
    guest_name = data.get('guest_name')

    booking = Booking(hotel_id=hotel_id, check_in_date=check_in_date, check_out_date=check_out_date, guest_name=guest_name)
    db.session.add(booking)
    db.session.commit()

    return jsonify({'message': 'Booking created successfully'}), 201

@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify([{'id': booking.id, 'hotel_id': booking.hotel_id, 'check_in_date': booking.check_in_date,
                     'check_out_date': booking.check_out_date, 'guest_name': booking.guest_name} for booking in bookings])
