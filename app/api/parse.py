from json import dumps, loads
from json.decoder import JSONDecodeError
from app.api.errors import error_message


def parse_input_data(request_data):
    try:
        json_data = request_data["results"]
        return (parse_hostname(json_data), parse_detected_os(json_data),
                parse_open_ports(json_data), parse_exploit_status(json_data),
                parse_other_info(json_data))
    except (JSONDecodeError, KeyError) as e:
        return error_message(e)


def parse_hostname(data):
    return data[1]["detected_system"]["other"]["hostname"]


def parse_detected_os(data):
    return data[1]["detected_system"]["detected_OS"]


def parse_exploit_status(data):
    return data[0]["exploit_status"]


def parse_open_ports(data):
    return data[1]["detected_system"]["open_ports"]


def parse_other_info(data):
    return data[1]["detected_system"]["other"]


def parse_results(tuple, original):
    #print(original)
    host, table = tuple
    #print(host)
    return {
        "results": {
            "uuid": host[1],
            "detection": {
                "detected_OS": original[1],
                "open_ports": original[2],
                "other": original[4]
            },
            "exploit_status": {
                original[3]["exploit"]: original[3]["successful"]
            }
        }
    }


def parse_auth_header(header):
    return header.get("Authorization").replace("Bearer", "").strip()
