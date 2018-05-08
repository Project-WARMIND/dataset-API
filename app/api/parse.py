from json import dumps, loads
from json.decoder import JSONDecodeError
from app.api.errors import unparseableJSON

def parse_input_data(data):
    try:
        data = str(data).strip()
        json_data = loads(data)
        print(str(json_data))
        return json_data["results"]
    except JSONDecodeError:
        return unparseableJSON
