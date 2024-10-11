# Extracted from https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
import json
data = json.loads('{"foo":1, "bar":2, "fiddle":{"bar":2, "foo":1}}')
print(json.dumps(data, indent=4))

{
    "fiddle": {
        "bar": 2,
        "foo": 1
    },
    "bar": 2,
    "foo": 1
}

{
    "foo": 1,
    "bar": 2,
    "fiddle": {
        "bar": 2,
        "foo": 1
    }
}

