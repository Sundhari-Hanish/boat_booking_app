from database.db import get_connection

def create_user(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users 
    (register_id, passenger_name, age, mobile, email, dob, gender, aadhar)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, data)

    conn.commit()
    conn.close()


def get_user(register_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE register_id=%s", (register_id,))
    user = cursor.fetchone()

    conn.close()
    return user
