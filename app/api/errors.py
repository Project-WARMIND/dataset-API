def error_message(error):
    return {"error": error}


def auth_error():
    return {"error": "There was a problem authentication"}


def invalid_uuid():
    return {"error": "Invalid uuid"}
