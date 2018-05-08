from json import dumps, loads
from json.decoder import JSONDecodeError
from app.api.errors import unparseableJSON


def parse_input_data(request_data):
    try:
        #data = str(request_data.decode('utf8').replace("'", '"')).strip()
        #json_data = loads(data)["results"]
        json_data = request_data["results"]
        return (
            parse_hostname(json_data),
            parse_detected_os(json_data),
            parse_open_ports(json_data),
            parse_exploit_status(json_data),
        )
    except JSONDecodeError:
        return unparseableJSON


def parse_hostname(data):
    return data[1]["detected system"]["other"]["hostname"]


def parse_detected_os(data):
    return data[1]["detected system"]["detected OS"]


def parse_exploit_status(data):
    return data[0]["exploit status"]


def parse_open_ports(data):
    return data[1]["detected system"]["open_ports"]


def parse_results(tuple, original):
    print(tuple)
    host, table = tuple
    return {
        host[1]: {
            "DETECTION": "some_value_and_ports_and_other_items",
            "EXPLOIT_SUCCESS": "some value"
        }
    }
