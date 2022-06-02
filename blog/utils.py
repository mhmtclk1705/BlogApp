import uuid

def get_random_code():
    code = str(uuid.uuid1())[:11].replace('-', '')
    return code
    