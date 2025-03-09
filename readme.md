# Booking Application

A Flask-based web application to manage bookings for members and inventory items.

## Features

- Upload and import CSV data for members and inventory
- Book items from inventory for members
- Cancel bookings
- View all members and inventory items

## Prerequisites

- Python 3.8+
- PostgreSQL

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/booking-app.git
cd booking-app
```

2. **Set up a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up PostgreSQL database**

Create a PostgreSQL database:

```bash
createdb booking_app
```

Or connect to PostgreSQL and create the database:

```sql
CREATE DATABASE booking_app;
```

5. **Configure environment variables**

Create a `.env` file in the project root:

```
DATABASE_URI=postgresql://username:password@localhost:5432/booking_app
```

Replace `username` and `password` with your PostgreSQL credentials.

6. **Initialize the database**

```bash
flask init-db
```

7. **Place CSV files in the data directory**

Create a `data` directory and place the CSV files:

```bash
mkdir -p data
cp path/to/members.csv data/
cp path/to/inventory.csv data/
```

8. **Import data from CSV files**

```bash
flask import-data
```

Alternatively, you can use the `/import` endpoint to import data.

9. **Run the application**

```bash
flask run
```

The application will be available at http://localhost:5000

## API Endpoints

### Import Data
```
POST /import
```

### Book an Item
```
POST /book
Content-Type: application/json

{
  "member_id": 1,
  "inventory_id": 1
}
```

### Cancel a Booking
```
POST /cancel
Content-Type: application/json

{
  "booking_reference": "booking-reference-uuid"
}
```

### View All Members
```
GET /members
```

### View All Inventory Items
```
GET /inventory
```

## Database Schema

The application uses three main tables:
- `members`: Stores information about members
- `inventory`: Stores information about bookable items
- `bookings`: Stores booking information, linking members and inventory items

## Business Rules

- A member can have a maximum of 2 active bookings
- An inventory item must have available count (remaining_count > 0) to be booked
- An inventory item cannot be booked if it has expired

## License

This project is licensed under the MIT License - see the LICENSE file for details.