import random
def generate_register_id():
    return "REG" + str(random.randint(10000, 99999))
def generate_transaction_id():
    return "TXN" + str(random.randint(100000, 999999))
