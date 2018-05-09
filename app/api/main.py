from flask import Flask, request, jsonify
from functools import wraps

from app.api.database import connection, create_host, get_host_info
from app.api.settings import config
from app.api.parse import parse_input_data, parse_results
from app.api.auth import is_auth
from app.api.errors import auth_error, invalid_uuid

app = Flask(__name__)
app.debug = config["debug"]
app.secret_key = config["secret_key"]

conn = connection()


def auth_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if is_auth(conn, request.headers):
            return test(*args, **kwargs)
        else:
            return jsonify(auth_error())

    return wrap


@app.route("/healthcheck", methods=["GET"])
def api_healthcheck():
    return jsonify({"health": "GOOD"})


@app.route("/host/<uuid>", methods=["GET"])
@auth_required
def api_get_host_info(uuid):
    if uuid.startswith('h') and not uuid == "hosts":
        return jsonify(get_host_info(conn, uuid))
    return jsonify(invalid_uuid())


@app.route("/hosts", methods=["POST"])
@auth_required
def api_create_host():
    data = parse_input_data(request.get_json())
    try:
        error = data["error"]
        return jsonify(data)
    except TypeError:
        results = create_host(
            conn,
            data[0],
            data[1],
            open_ports=data[2],
            exploit_status=data[3],
            other=data[4],
            test=request.headers.get("Test-Case"))
        return jsonify(parse_results(results, data))


def start_flask():
    app.run(port=config["port"])
