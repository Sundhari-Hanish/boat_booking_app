from flask import Blueprint, request, render_template, session
from services.admin_service import create_boat, create_route, change_price, fetch_price
admin_bp = Blueprint("admin", __name__)
ADMIN_PASSWORD = "admin123"
@admin_bp.route("/", methods=["GET", "POST"])
def admin_page():
    message = None

    # Handle login

    if request.method == "POST":
        action = request.form.get("action")

        if action == "login":
            password = request.form.get("password")

            if password == ADMIN_PASSWORD:
                session["admin_logged_in"] = True
                message = "Login successful ✅"
            else:
                message = "Wrong password ❌"


        # Admin actions (Only after login)

        elif session.get("admin_logged_in"):

            if action == "add_boat":
                name = request.form.get("boat_name")
                capacity = request.form.get("capacity")

                if not name or not capacity:
                    message = "Fill all boat details ❌"
                else:
                    create_boat(name, int(capacity))
                    message = "Boat added ✅"

            elif action == "add_route":
                source = request.form.get("source")
                destination = request.form.get("destination")

                if not source or not destination:
                    message = "Fill route details ❌"
                else:
                    create_route(source, destination)
                    message = "Route added ✅"

            elif action == "update_price":
                price = request.form.get("price")

                if not price:
                    message = "Enter price ❌"
                else:
                    change_price(int(price))
                    message = "Price updated ✅"

        else:
            message = "Please login first ❌"

    price = fetch_price()

    return render_template(
        "admin.html",
        price=price,
        message=message,
        logged_in=session.get("admin_logged_in")
    )
