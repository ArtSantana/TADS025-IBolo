import json
from types import SimpleNamespace

class ResponseGeneric:
    def __init__(self):
        self.data = SimpleNamespace()
        self.status = 200

    def get_body_json(self):
        jsonResponse = json.dumps(self.data.__dict__)
        return jsonResponse