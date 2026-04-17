from flask import Blueprint, request, render_template
from services.booking_service import book_ticket
from services.user_service import register_user, fetch_user
from models.admin_model import get_boats, get_routes, get_price
from datetime import datetime

customer_bp = Blueprint("customer", __name__)

@customer_bp.route("/", methods=["GET", "POST"])
def customer_page():
    boats = get_boats()
    routes = get_routes()
    price = get_price()

    user_data = None
    message = None
    reg_id = None

    if request.method == "POST":

        user_type = request.form.get("user_type")
        reg_id = request.form.get("register_id")

        # Existing user fetch

        if user_type == "existing" and reg_id:
            user_data = fetch_user(reg_id)

            if not user_data:
                return "Invalid Register ID ❌"

        # booking
        if request.form.get("action") == "book":

            name = request.form.get("name")
            age = request.form.get("age")
            mobile = request.form.get("mobile")
            email = request.form.get("email")
            dob = request.form.get("dob") or None
            gender = request.form.get("gender")
            aadhar = request.form.get("aadhar")

            source = request.form.get("source")
            destination = request.form.get("destination")
            boat = request.form.get("boat")
            seats = int(request.form.get("seats"))

            total_price = seats * price

            #handling user type
            if user_type == "new":
                reg_id = register_user(
                    (name, age, mobile, email, dob, gender, aadhar)
                )

            elif user_type == "existing":
                if not reg_id:
                    return "Please enter Register ID ❌"

            #book ticket
            txn_id = book_ticket(
                (name, age, mobile, email, dob, gender, aadhar),
                (
                    source,
                    destination,
                    datetime.now().date(),
                    datetime.now().strftime("%H:%M:%S"),
                    boat,
                    seats,
                    total_price,
                ),
            )


            #success message
            message = {
                "txn_id": txn_id,
                "reg_id": reg_id,
                "name": name,
                "source": source,
                "destination": destination,
                "boat": boat,
                "seats": seats,
                "price": total_price,
            }

    return render_template(
        "customer.html",
        boats=boats,
        routes=routes,
        price=price,
        user=user_data,
        message=message,
    )
