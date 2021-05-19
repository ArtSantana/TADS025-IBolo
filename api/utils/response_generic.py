import json
from json.encoder import JSONEncoder
from types import SimpleNamespace

class ResponseGeneric:
    def __init__(self):
        self.data = SimpleNamespace()
        self.status = 200

    def get_body_json(self) -> JSONEncoder:
        jsonResponse = json.dumps(self.data.__dict__)
        return jsonResponse

    def set_message_and_status(self, message: str, status: int) -> None:
        self.status = status
        self.data.message = message