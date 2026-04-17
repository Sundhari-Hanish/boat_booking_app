from models.admin_model import add_boat, add_route, update_price, get_price

def create_boat(name, capacity):
    add_boat(name, capacity)

def create_route(source, destination):
    add_route(source, destination)

def change_price(price):
    update_price(price)

def fetch_price():
    return get_price()
