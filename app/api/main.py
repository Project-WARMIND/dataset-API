from flask import Flask, request, jsonify

from app.api.database import connection, create_host
from app.api.settings import config
from app.api.parse import parse_input_data

app = Flask(__name__)
app.debug = config["debug"]
app.secret_key = config["secret_key"]

conn = connection()

@app.route('/host', methods=['POST'])
def api_create_host():
    data = parse_input_data(request.data)
    try:
        error = data["error"]
        return jsonify(data)
    except TypeError:
        return create_host(data)

def start_flask():
    app.run(port=config["port"])
