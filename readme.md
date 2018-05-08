# dataset-API

Tested using Python 3.6

## Install

Add `migrate.sql` to your database and update `./app/api/settings.py` with credentials

```bash
virtualenv venv --python=python3.6
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Task

Takes:

```json
{
  "results": [{
      "exploit_status": {
        "exploit": "CVE-NAME",
        "successful": true
      }
    },
    {
      "detected_system": {
        "detected_OS": "Windows 7",
        "open_ports": [
          1,
          2,
          3
        ],
        "other": {
          "hostname": "test",
          "ip_address": "127.0.0.1",
          "random_key": "value"
        },
        "windows_size": [
          [
            123,
            123
          ],
          [
            123,
            123
          ]
        ]
      }
    }
  ]
}

```

Returns:

```json
{
    "results": {
        "detection": {
            "detectedOS": "Windows 7",
            "openPorts": [
                1,
                2,
                3
            ],
            "other": {
                "hostname": "test",
                "ip_address": "127.0.0.1",
                "random_key": "value"
            }
        },
        "exploitSuccess": {
            "CVE-NAME": true
        },
        "uuid": "h68d3c6d15fb846d4b00cf5a011447b88"
    }
}
```
