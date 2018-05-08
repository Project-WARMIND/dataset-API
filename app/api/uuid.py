from uuid import uuid4, uuid1

def generate_uuid():
    return str('h' + uuid4().hex)

def generate_host():
    return str("host_" + uuid1().hex)
