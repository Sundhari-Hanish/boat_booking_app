from utils.helpers import generate_register_id
from models.user_model import create_user, get_user

def register_user(user_data):
    reg_id = generate_register_id()
    create_user((reg_id, *user_data))
    return reg_id

def fetch_user(reg_id):
    return get_user(reg_id)
