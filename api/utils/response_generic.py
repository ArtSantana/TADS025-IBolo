import json
from types import SimpleNamespace

class ResponseGeneric:
    def __init__(self, message: str, status: int):
        self.__data = SimpleNamespace()
        self.message = message
        self.status = status

    def get_body_json(self):
        self.__data.status = self.status
        self.__data.message = self.message
        jsonResponse = json.dumps(self.__data.__dict__)
        return jsonResponse