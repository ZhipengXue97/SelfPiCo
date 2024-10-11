# Extracted from https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object
from marshmallow_dataclass import dataclass

@dataclass
class User:
    name: str

user = User.Schema().load({"name": "Ramirez"})

