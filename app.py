from flask import Flask, request, jsonify
from models import db, Member, Inventory, Booking
from config import Config
from utils import import_members_csv, import_inventory_csv
from datetime import datetime
import os
import ssl

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)


# Configure SSL context for PostgreSQL connection if required
if 'sslmode=require' in app.config['SQLALCHEMY_DATABASE_URI']:
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    connect_args = {'sslmode': 'require', 'sslcontext': ssl_context}
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': connect_args}
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {'sslmode': 'require'}  
}

# Initialize database
db.init_app(app)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200

@app.route('/import', methods=['POST'])
def import_data():
    """Import data from CSV files."""
    try:
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Get file paths from request or use default paths
        members_file = request.form.get('members_file', 'data/members.csv')
        inventory_file = request.form.get('inventory_file', 'data/inventory.csv')
        
        # Import data
        with app.app_context():
            import_members_csv(members_file)
            import_inventory_csv(inventory_file)
        
        return jsonify({"message": "Data imported successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/book', methods=['POST'])
def book_item():
    """Book an item from inventory."""
    try:
        data = request.json
        member_id = data.get('member_id')
        inventory_id = data.get('inventory_id')
        
        # Validate request data
        if not member_id or not inventory_id:
            return jsonify({"error": "Member ID and Inventory ID are required"}), 400
        
        # Get member and inventory item
        member = Member.query.get(member_id)
        inventory_item = Inventory.query.get(inventory_id)
        
        if not member:
            return jsonify({"error": "Member not found"}), 404
        
        if not inventory_item:
            return jsonify({"error": "Inventory item not found"}), 404
        
        # Check if member has reached maximum bookings
        if member.booking_count >= Config.MAX_BOOKINGS:
            return jsonify({"error": "Member has reached maximum bookings"}), 400
        
        # Check if inventory has remaining items
        if inventory_item.remaining_count <= 0:
            return jsonify({"error": "No items remaining in inventory"}), 400
        
        # Check if inventory item has expired
        if inventory_item.expiration_date < datetime.now().date():
            return jsonify({"error": "Inventory item has expired"}), 400
        
        # Create booking
        booking = Booking(
            member_id=member.id,
            inventory_id=inventory_item.id
        )
        
        # Update member and inventory
        member.booking_count += 1
        inventory_item.remaining_count -= 1
        
        # Save to database
        db.session.add(booking)
        db.session.commit()
        
        return jsonify({
            "message": "Booking successful",
            "booking_reference": booking.booking_reference,
            "member": f"{member.name} {member.surname}",
            "item": inventory_item.title
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/cancel', methods=['POST'])
def cancel_booking():
    """Cancel a booking."""
    try:
        data = request.json
        booking_reference = data.get('booking_reference')
        
        # Validate request data
        if not booking_reference:
            return jsonify({"error": "Booking reference is required"}), 400
        
        # Get booking
        booking = Booking.query.filter_by(booking_reference=booking_reference, is_active=True).first()
        
        if not booking:
            return jsonify({"error": "Active booking not found"}), 404
        
        # Get member and inventory
        member = Member.query.get(booking.member_id)
        inventory_item = Inventory.query.get(booking.inventory_id)
        
        # Mark booking as inactive
        booking.is_active = False
        
        # Update member and inventory
        member.booking_count -= 1
        inventory_item.remaining_count += 1
        
        # Save to database
        db.session.commit()
        
        return jsonify({
            "message": "Booking cancelled successfully",
            "booking_reference": booking.booking_reference
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/members', methods=['GET'])
def get_members():
    """Get all members."""
    members = Member.query.all()
    members_list = [{
        "id": member.id,
        "name": member.name,
        "surname": member.surname,
        "booking_count": member.booking_count,
        "date_joined": member.date_joined.isoformat()
    } for member in members]
    
    return jsonify({"members": members_list}), 200

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Get all inventory items."""
    items = Inventory.query.all()
    items_list = [{
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "remaining_count": item.remaining_count,
        "expiration_date": item.expiration_date.isoformat()
    } for item in items]
    
    return jsonify({"inventory": items_list}), 200

@app.cli.command("init-db")
def init_db_command():
    """Create database tables."""
    with app.app_context():
        db.create_all()
        print("Database tables created.")

@app.cli.command("import-data")
def import_data_command():
    """Import data from CSV files."""
    with app.app_context():
        import_members_csv('data/members.csv')
        import_inventory_csv('data/inventory.csv')

if __name__ == '__main__':
    app.run(debug=True)