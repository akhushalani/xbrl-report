import os
import json


def read_secrets():
    filepath = os.path.join('secrets.json')
    try:
        with open(filepath) as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}
