from flask import Flask
from routes.customer_routes import customer_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.secret_key = "secret123"
app.register_blueprint(customer_bp, url_prefix="/customers")
app.register_blueprint(admin_bp, url_prefix="/admin")

if __name__ == "__main__":
    app.run(debug=True)
