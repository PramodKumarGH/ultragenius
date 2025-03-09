import csv
from datetime import datetime
from models import db, Member, Inventory

def parse_date(date_str):
    """Parse date strings from CSV files."""
    # Handle ISO format for members.csv
    if 'T' in date_str:
        return datetime.fromisoformat(date_str)
    
    # Handle DD/MM/YYYY format for inventory.csv
    else:
        return datetime.strptime(date_str, '%d/%m/%Y')

def import_members_csv(file_path):
    """Import members from CSV file."""
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Check if member with same name and surname already exists
            existing_member = Member.query.filter_by(
                name=row['name'].strip(), 
                surname=row['surname'].strip()
            ).first()
            
            if not existing_member:
                member = Member(
                    name=row['name'].strip(),
                    surname=row['surname'].strip(),
                    booking_count=int(row['booking_count']),
                    date_joined=parse_date(row['date_joined'])
                )
                db.session.add(member)
    
    db.session.commit()
    print("Members import completed.")

def import_inventory_csv(file_path):
    """Import inventory items from CSV file."""
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Check if inventory with same title already exists
            existing_item = Inventory.query.filter_by(title=row['title'].strip()).first()
            
            if not existing_item:
                inventory = Inventory(
                    title=row['title'].strip(),
                    description=row['description'].strip(),
                    remaining_count=int(row['remaining_count']),
                    expiration_date=parse_date(row['expiration_date'])
                )
                db.session.add(inventory)
    
    db.session.commit()
    print("Inventory import completed.")