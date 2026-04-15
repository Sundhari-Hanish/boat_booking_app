from database.db import get_connection

def add_boat(name, capacity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO boats (boat_name, capacity) VALUES (%s, %s)", (name, capacity))
    conn.commit()
    conn.close()

def add_route(source, destination):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO routes (source, destination) VALUES (%s, %s)", (source, destination))
    conn.commit()
    conn.close()

def get_boats():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT boat_name FROM boats")
    boats = [row[0] for row in cursor.fetchall()]
    conn.close()
    return boats

def get_routes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT source, destination FROM routes")
    routes = cursor.fetchall()
    conn.close()
    return routes

def update_price(price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE pricing SET price_per_seat=%s", (price,))
    conn.commit()
    conn.close()

def get_price():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT price_per_seat FROM pricing LIMIT 1")
    price = cursor.fetchone()[0]
    conn.close()
    return price
