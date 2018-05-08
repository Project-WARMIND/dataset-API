from flask import Flask, request, jsonify

from app.api.database import connection, create_host
from app.api.settings import config
from app.api.parse import parse_input_data, parse_results

app = Flask(__name__)
app.debug = config["debug"]
app.secret_key = config["secret_key"]

conn = connection()


@app.route('/host', methods=['POST'])
def api_create_host():
    data = parse_input_data(request.get_json())
    print(data)
    try:
        error = data["error"]
        return jsonify(data)
    except TypeError:
        if not request.headers.get('Test-Status'):
            results = create_host(
                conn,
                data[0],
                data[1],
                open_ports=data[2],
                exploit_status=data[3])
            return jsonify(parse_results(results, data))
        else:
            print(data)
            return jsonify(data)


def start_flask():
    app.run(port=config["port"])
