from app.api.database import psql_command
from app.api.parse import parse_auth_header
from app.api.uuid import generate_token


def token_in_db(conn, token):
    response = psql_command(
        conn, "SELECT * FROM tokens WHERE token = %s", values=(token, ))
    return (response and "hosts" in response[3])


def is_auth(conn, header):
    token = parse_auth_header(header)
    return token_in_db(conn, token)


def add_token():
    return generate_token()
