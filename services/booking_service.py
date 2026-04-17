from models.booking_model import create_booking, get_all_bookings
from utils.helpers import generate_transaction_id
from datetime import datetime

def book_ticket(user_data, travel_data):
    txn_id = generate_transaction_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = (
        txn_id,
        *user_data,
        *travel_data,
        "SUCCESS",
        "CONFIRMED",
        timestamp
    )

    create_booking(data)
    return txn_id

def fetch_bookings():
    return get_all_bookings()
